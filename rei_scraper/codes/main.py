from scraper.immoscout_scraper import scrape_listings
from scraper.send_to_make import send_listing_to_make

def main():
    listings = scrape_listings()

    for listing in listings:
        send_listing_to_make(listing)

if __name__ == "__main__":
    main()
