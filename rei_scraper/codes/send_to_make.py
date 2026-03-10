import os
import requests

MAKE_WEBHOOK_URL = os.getenv("MAKE_WEBHOOK_URL")

def send_listing_to_make(listing: dict):
    if not MAKE_WEBHOOK_URL:
        raise ValueError("MAKE_WEBHOOK_URL is not set")

    response = requests.post(MAKE_WEBHOOK_URL, json=listing, timeout=30)
    response.raise_for_status()
