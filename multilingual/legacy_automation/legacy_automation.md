# Legacy Multilingual Customer Support Automation (2025)

This project documents a legacy multilingual customer support automation workflow implemented in 2025 before a native integration for Zammad became available in Make.com.

The system enabled a German-speaking support team to communicate with customers who submitted support requests in different languages. Incoming messages were automatically translated into German for internal use, and agent responses were translated back into the customer's original language before being delivered.

Because Zammad did not yet have a native integration in Make.com at the time, most automation logic—including translation, ticket processing, tagging, categorization, and logging—was implemented directly inside Make using webhooks and API calls.

All interactions with Zammad were handled through the **Zammad REST API via the HTTP module**.

---

## System Overview

The automation served as a translation and classification layer between customer messages and the internal support team.

The workflow consisted of two core processes:

**Use Case 1 – Inbound Ticket Translation**  
Customer messages written in various languages were translated into German so that support agents could process all tickets using a single internal language.
https://github.com/krsnp5/make_usecases/blob/main/multilingual/legacy_automation/LEG_UC1_Inbound_Translation.png

**Use Case 2 – Outbound Ticket Translation**  
Responses written by support agents in German were automatically translated back into the customer's original language before being sent.
https://github.com/krsnp5/make_usecases/blob/main/multilingual/legacy_automation/LEG_UC2_Outbound_Translation.png

Together, these workflows created a fully automated multilingual support pipeline.

---

## Use Case 1 – Inbound Ticket Translation

When a new support ticket was created, the automation performed the following steps:

1. Receive ticket data via webhook  
2. Detect the language of the incoming message  
3. Translate the message into German  
4. Add a language tag to the ticket  
5. Categorize the ticket using business rules  
6. Log translation activity for monitoring and reporting  

This allowed support agents to view both the **original message and the translated German version** within the same ticket.

### Anti-Loop Protection

An anti-loop safeguard prevented the automation from repeatedly triggering itself when ticket updates were written back into Zammad.

This ensured that translated comments or tags did not cause recursive automation runs.

### Ticket Categorization

The automation applied business rules to classify the ticket and assign appropriate category tags.

Depending on the evaluation, the system could:

- assign a single category  
- assign multiple categories  
- trigger rule-based tagging  

These categories were applied to the ticket through Zammad API calls.

---

## Use Case 2 – Outbound Ticket Translation

When a support agent responded to a ticket, the automation ensured that the reply was translated back into the customer's original language.

The workflow performed the following actions:

1. Receive ticket update via webhook  
2. Retrieve ticket language tags  
3. Identify the customer's original language  
4. Extract the reply message content  
5. Translate the reply from German to the customer's language  
6. Add the translated response back into the ticket as a comment  
7. Log the translation activity  

This ensured that customers always received replies in their native language while agents continued working entirely in German.

---

## Logging and Monitoring

Automation activity was logged to Google Sheets for operational visibility and auditing.

Logs recorded information such as:

- ticket ID  
- detected language  
- translation output  
- agent identifier  
- processing timestamp  

This allowed the team to monitor translation performance and automation activity.

---

## Technology Stack

- Make.com  
- OpenAI API  
- Zammad REST API (via HTTP module)  
- Google Sheets (logging and monitoring)

Because Zammad was not yet available as a native Make.com application at the time, most workflow orchestration and ticket-processing logic had to be implemented directly inside Make.

---

## Legacy Implementation Notes

This automation represents an early implementation of a multilingual support system built using APIs and automation tools when direct platform integrations were not yet available.

The workflow demonstrates how helpdesk platforms can still be integrated into automation systems using webhooks and API calls.

---

## Disclaimer

This repository contains a **reconstructed demonstration of automation concepts inspired by real-world implementations** that were originally developed for organizations under **Non-Disclosure Agreements (NDAs)**.

To honor those agreements, the workflows shown here do not replicate the exact production infrastructure, datasets, integrations, or operational environments used in the original systems. Instead, they illustrate the architectural approach using simplified logic and publicly available tools.

All examples in this repository are provided strictly for **portfolio and educational purposes**.
