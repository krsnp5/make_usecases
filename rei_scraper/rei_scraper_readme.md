# REI Listing Intake & Price Change Detection Automation

## Overview

This project demonstrates an automated workflow for ingesting real estate listing data, detecting listing price changes, and synchronizing updates with a CRM pipeline.

The system combines a **Python-based scraper**, a **Make.com automation workflow**, and **GoHighLevel (GHL)** as the CRM layer.

The automation performs the following tasks:

- Collects listing data from a scraper
- Prevents duplicate listings from entering the CRM
- Monitors previously captured listings for price changes
- Automatically updates CRM contacts and opportunities when listing prices change

This architecture simulates how real estate acquisition teams track listing activity and maintain an up-to-date pipeline of potential deals.

---

# System Architecture

The workflow is divided into multiple components with clear responsibilities.

Render Cron Job
↓
Python Scraper
↓
POST → Make Webhook
↓
Listing Intake Automation
↓
Data Store (listing state memory)
↓
GoHighLevel CRM


Responsibilities are separated across the system:

| Component | Role |
|--------|------|
| Render | scheduled execution environment |
| Python | listing data extraction |
| Make.com | automation, routing, and change detection |
| Data Store | listing state memory |
| GoHighLevel | contact and opportunity tracking |

---

# Automation Workflow

The Make scenario is responsible for ingesting listings, detecting duplicates, and identifying price changes.

## 1. Listing Intake

The scraper sends listing data to a Make webhook.

Example payload:

```json
{
  "source_platform": "immoscout24",
  "listing_id": "12345",
  "listing_title": "Detached house with garden",
  "listing_url": "https://example.com/listing/12345",
  "price_numeric": 120000,
  "property_type": "single_family",
  "city": "Leipzig"
}
```

## 2. Listing Deduplication

The automation checks a Make Data Store to determine whether the listing has already been processed.

A unique key is generated for each listing:

```json

dedupe_key = source_platform + "_" + listing_id

```

If the listing has not been seen before:

- it is stored in the listing memory
- a contact is created in GoHighLevel
- an opportunity is created in the acquisition pipeline

## 3. Listing State Tracking

Previously processed listings are stored in a Make Data Store to allow the automation to track listing state across multiple scraper runs.

Stored attributes include:

- dedupe_key
- listing_url
- current_price
- property_type
- city
- source_platform
- last_seen

This allows the system to compare new scraper results with previously recorded listing data.

---

## 4. Price Change Detection

If an existing listing reappears in the scraper output, the automation compares the incoming price with the stored price.

Condition used in the automation:

```json

incoming_price != stored_price

```

If the price has changed:

1. the stored record is updated  
2. the CRM contact is updated  
3. the CRM opportunity is updated  

This ensures that the CRM always reflects the latest listing price without creating duplicate leads.

---

# CRM Synchronization

The automation maintains synchronization with GoHighLevel by updating both contacts and opportunities.

## Contact Updates

Fields may include:

- listing URL  
- property type  
- city  
- current asking price  
- last detected price change  

## Opportunity Updates

The opportunity represents the potential acquisition lead.

Updates include:

- opportunity value (asking price)  
- updated listing data  
- optional pipeline stage changes  

---

# Data Store Design

The automation uses a Make Data Store to maintain listing state.

Example structure:

| Field | Description |
|------|-------------|
| dedupe_key | unique listing identifier |
| listing_url | original listing link |
| price | latest known listing price |
| city | property location |
| source_platform | listing source |
| last_seen | timestamp of last scrape |

This memory layer enables both **deduplication** and **price change detection**.

---

# Scenario Logic

The Make automation follows this logical flow:

Webhook Trigger
↓
Normalize listing data
↓
Check Data Store for existing record
↓
Router
├─ New Listing
│ ↓
│ Store listing
│ ↓
│ Create CRM contact
│ ↓
│ Create CRM opportunity
│
└─ Existing Listing
↓
Check for price change
├─ No change → end
└─ Price changed
↓
Update stored listing
↓
Update CRM contact
↓
Update CRM opportunity


---

# Technologies Used

- Python  
- Requests  
- BeautifulSoup  
- Render (Cron Jobs)  
- Make.com  
- GoHighLevel CRM  

---

# Key Automation Patterns Demonstrated

This project demonstrates several automation and data engineering patterns:

- webhook-based ingestion  
- stateful data processing  
- deduplication pipelines  
- change detection workflows  
- CRM synchronization  
- event-driven automation  

These patterns are commonly used in real-world automation systems, lead ingestion pipelines, and property acquisition tools.

---

# Disclaimer

This project represents a **simulated reconstruction of automation workflows inspired by real-world implementations** developed for companies under **Non-Disclosure Agreements (NDAs)**.

To honor those agreements, the code and workflows presented here do **not replicate the exact production systems, integrations, datasets, or infrastructure** used in the original environments.

Instead, the project demonstrates the **automation architecture and technical concepts** using publicly available tools and simplified logic.

All examples in this repository are intended solely for **portfolio and educational purposes**.
