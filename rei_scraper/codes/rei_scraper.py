import requests
from bs4 import BeautifulSoup
import json
import time

from config import MAKE_WEBHOOK, BASE_URL, HEADERS


def fetch_listings():
    response = requests.get(BASE_URL, headers=HEADERS, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    listings = []

    cards = soup.select("article")  # listing cards

    for card in cards:

        title = card.get_text(strip=True)

        link = card.find("a")
        if not link:
            continue

        listing_url = "https://www.immobilienscout24.de" + link.get("href", "")

        price = None
        price_element = card.select_one('[data-testid="price"]')
        if price_element:
            price = price_element.get_text(strip=True)

        listings.append({
            "source": "immoscout24",
            "title": title,
            "listing_url": listing_url,
            "price": price
        })

    return listings


def send_to_make(listing):

    payload = {
        "source": "immoscout24",
        "title": listing["title"],
        "listing_url": listing["listing_url"],
        "price": listing["price"]
    }

    r = requests.post(MAKE_WEBHOOK, json=payload, timeout=30)

    if r.status_code == 200:
        print("Sent to Make:", listing["title"])
    else:
        print("Error sending to Make:", r.text)


def main():

    listings = fetch_listings()

    print(f"Found {len(listings)} listings")

    for listing in listings:
        send_to_make(listing)
        time.sleep(2)


if __name__ == "__main__":
    main()
