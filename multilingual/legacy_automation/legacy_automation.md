# Legacy Multilingual Customer Support Automation (2025)

This project documents a legacy automation workflow built in 2025 to enable multilingual customer support operations before a native integration for Zammad became available in Make.com.

The goal of the system was to allow a **German-speaking support team** to communicate with customers who send inquiries in different languages without requiring agents to manually translate messages.

At the time the workflow was created, **Zammad did not yet have a native Make.com integration**, so the automation relied on webhooks and API calls to connect the helpdesk system with translation services.

---

## System Overview

The automation acted as a translation bridge between customer messages and the internal support team.

Customer inquiries arriving in different languages were automatically translated into German so the internal support team could work in a single operating language. Responses written by agents in German were then translated back into the customer's original language before being sent out.

The system used **Make.com for workflow orchestration**, **OpenAI for translation**, and **Zammad's REST API** to interact with the helpdesk platform.

Because a direct integration was not yet available in Make.com at the time, **Zammad API endpoints were connected through the HTTP module**, allowing the automation to retrieve ticket data and update tickets programmatically.

---

## Key Capabilities

### Incoming Message Translation

When a customer submitted a support request in their native language, the message was processed by the automation workflow and translated into German.

Both the **original message and the German translation** were stored in the ticket so agents could view the full context of the communication.

This allowed the support team to operate entirely in German while still supporting customers from multiple regions.

---

### Automated Acknowledgement Messages

Upon receiving a new customer inquiry, the system automatically generated an acknowledgement message.

The acknowledgement was translated into the **customer's original language** before being sent, informing the customer that their request had been received and that a support agent would respond within the expected service window.

---

### Agent Reply Translation

When support agents responded in German, the system automatically translated the reply into the customer's original language.

This ensured that customers received responses in their native language while agents continued working within their standard German-language support workflow.

---

## Technology Stack

- Make.com  
- OpenAI API  
- Zammad REST API  
- HTTP module (for API communication)

Since Zammad was not yet available as a native Make.com app at the time of implementation, **API requests were handled through the HTTP module**, allowing the automation to fetch, create, and update ticket data through the Zammad API.

---

## Legacy Implementation Notes

This version of the automation reflects an earlier implementation of the multilingual support workflow. Since then, the platform ecosystem has evolved and newer integrations may simplify or replace parts of the architecture.

The legacy workflow demonstrates how multilingual support automation can be implemented using APIs and automation platforms even when direct integrations are not available.

---

## Disclaimer

This repository contains a **reconstructed demonstration of automation concepts inspired by real-world implementations** that were originally developed for companies under **Non-Disclosure Agreements (NDAs)**.

To honor those agreements, the workflows shown here do not replicate the exact production infrastructure, datasets, integrations, or operational environments used in the original systems. Instead, they illustrate the architectural approach using simplified logic and publicly available tools.

All examples in this repository are provided strictly for **portfolio and educational purposes**.
