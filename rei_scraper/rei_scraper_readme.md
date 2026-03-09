# ImmoScout24 Listing Intake Automation

This project demonstrates a Python-based workflow for extracting publicly available real estate listing information and integrating it with an automation pipeline for lead qualification and CRM tracking.

The scraper collects listing data from ImmoScout24 and sends structured information to **Make.com**, where automation workflows apply qualification rules and create corresponding records in **GoHighLevel (GHL)**.

The goal of the system is to assist real estate acquisition teams in identifying potential opportunities while ensuring that all outreach activity is tracked in a centralized CRM pipeline.

---

## System Overview

The workflow combines a Python scraper with an automation layer built in Make.com.

The Python component extracts listing data and sends it to a Make webhook. The Make scenario then evaluates the listing against predefined acquisition criteria and records the opportunity in GoHighLevel.

Responsibilities are separated across the system:

- **Python** handles listing extraction and data preparation  
- **Make.com** performs business rule evaluation and routing  
- **GoHighLevel** manages contacts, opportunities, and acquisition pipeline tracking  

---

## Extracted Listing Data

The scraper collects key listing attributes such as:

- listing title  
- listing URL  
- asking price  
- property location (when available)  
- property type (when available)  
- source platform  

These attributes are sent to a Make webhook where the automation scenario processes the listing and determines the appropriate CRM action.

---

## CRM Integration

Once listing data reaches the Make automation scenario, the workflow performs the following steps:

1. Apply acquisition qualification rules  
2. Check for duplicate listings in the CRM  
3. Create or update a **GoHighLevel contact**  
4. Create a corresponding **GoHighLevel opportunity**

Each outreach event associated with a listing creates a matching opportunity record in GoHighLevel so that acquisition teams can track communication and deal progress within the CRM pipeline.

---

## Example Qualification Rules

Listings may be filtered using business rules such as:

- single-family homes only  
- no condos  
- no commercial properties  
- minimum property value thresholds  
- acceptable geographic regions  

These rules are evaluated within the Make automation layer before opportunities are created.

---

## Technologies Used

- Python  
- Requests  
- BeautifulSoup  
- Make.com  
- GoHighLevel CRM  

---

## Disclaimer

This project represents a **simulated reconstruction of automation workflows inspired by real-world implementations** that were originally developed for companies under **Non-Disclosure Agreements (NDAs)**.

To honor those agreements, the code and workflows presented here do **not replicate the exact production systems, integrations, datasets, or infrastructure** used in the original environments. Instead, the project demonstrates the general automation architecture and technical concepts using publicly available tools and simplified logic.

All examples in this repository are intended solely for **portfolio and educational purposes**.
