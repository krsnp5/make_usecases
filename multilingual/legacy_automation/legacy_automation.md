# Legacy Multilingual Ticket Translation Automation (2025)

This project documents a legacy automation workflow built in 2025 to support multilingual customer service operations before a native integration for Zammad became available in Make.com.

The system enabled a German-speaking support team to receive and process customer inquiries written in multiple languages. Incoming messages were automatically detected, translated, categorized, and logged so that support agents could work using a single internal language.

Because Zammad did not yet have a native Make.com integration at the time of implementation, the workflow relied on **webhooks and API calls through the HTTP module** to interact with the Zammad helpdesk system.

---

## System Overview

The automation acted as a translation and classification layer between customer messages and the internal support team.

When a new ticket was created in Zammad, the workflow performed the following actions:

1. Receive the ticket via webhook  
2. Detect the language of the customer message  
3. Translate the message into German  
4. Add a language tag to the ticket  
5. Apply ticket categories based on business rules  
6. Log the translation activity for monitoring and reporting  

This allowed support agents to view both the original message and the translated version directly within the ticket.

---

## Key Automation Components

### Ticket Webhook Trigger

A webhook triggered the workflow whenever a new ticket was created in Zammad. The ticket content and metadata were passed into the automation scenario for processing.

---

### Anti-Loop Protection

An anti-loop safeguard prevented the automation from repeatedly triggering itself when ticket updates were written back into the system.

This ensured that translated comments or tags added to the ticket did not cause recursive automation runs.

---

### Language Detection and Translation

The system automatically detected the language of the incoming message and generated a German translation so the support team could process tickets using their internal operating language.

---

### Ticket Language Tagging

The automation added a language tag to the ticket using the **Zammad REST API**.

Since Zammad was not yet available as a native Make.com application, API calls were executed using the **HTTP module** to update ticket metadata and comments.

---

### Ticket Categorization

Business rules were applied to determine how the ticket should be categorized.

Depending on the content and classification results, the system could:

- assign a single category  
- assign multiple categories  
- trigger rule-based tagging  

These categories helped route tickets to the appropriate support workflows.

---

### Translation Logging

The workflow also created translation logs in Google Sheets to track automation activity and provide audit visibility.

The log included information such as:

- ticket ID  
- detected language  
- translation output  
- processing timestamp  

---

## Technology Stack

- Make.com  
- OpenAI API  
- Zammad REST API (via HTTP module)  
- Google Sheets (logging and monitoring)

---

## Legacy Implementation Notes

This workflow represents the original implementation of the multilingual support automation before a native Zammad integration became available in Make.com.

The system demonstrates how automation platforms can integrate with external services through APIs even when direct connectors are not available.

---

## Disclaimer

This repository contains a **reconstructed demonstration of automation concepts inspired by real-world implementations** that were originally developed for organizations under **Non-Disclosure Agreements (NDAs)**.

To honor those agreements, the workflows shown here do not replicate the exact production infrastructure, datasets, integrations, or operational environments used in the original systems. Instead, they illustrate the architectural approach using simplified logic and publicly available tools.

All examples in this repository are provided strictly for **portfolio and educational purposes**.
