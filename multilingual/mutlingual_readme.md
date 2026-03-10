# Multilingual Customer Support Automation  
## Legacy Implementation (2025) and Modern Simulation

This project documents a multilingual customer support automation system originally implemented in 2025, along with a simulated modern implementation using the native Zammad integration in Make.com.

The system allowed a **German-speaking support team** to communicate with customers who submitted support requests in different languages. Incoming messages were translated into German for internal use, and agent replies were translated back into the customer's original language.

---

# Legacy Implementation (2025)

When the system was originally implemented, **Zammad did not yet have a native integration in Make.com**. Because of this limitation, most of the automation logic had to be implemented directly inside Make using webhooks, API calls, and routing logic.

The automation relied on the **Zammad REST API accessed through the HTTP module** to read and update ticket data.

This meant that tasks normally handled by helpdesk platforms—such as tagging, categorization, translation logging, and response handling—were orchestrated externally through Make.

---

## Use Case 1 — Inbound Ticket Translation

When a new ticket was created in Zammad, the automation performed the following steps:

1. Receive ticket data via webhook  
2. Detect the language of the incoming message  
3. Translate the message into German  
4. Add a language tag to the ticket  
5. Apply ticket categorization rules  
6. Log the translation for monitoring  

This allowed support agents to view both the **original customer message** and the **translated German version** within the same ticket.

### Anti-Loop Protection

Because ticket updates were written back into Zammad through the API, an anti-loop safeguard was required to prevent recursive automation triggers.

---

## Use Case 2 — Outbound Ticket Translation

When a support agent replied to a ticket, the system translated the response back into the customer's original language.

The workflow included:

1. Detect ticket update via webhook  
2. Retrieve ticket language tags  
3. Identify the customer's original language  
4. Extract the agent's message  
5. Translate the message into the customer's language  
6. Post the translated message back into the ticket via API  
7. Log the translation event  

This ensured that customers received responses in their native language while support agents continued working entirely in German.

---

## Logging and Monitoring

Automation activity was logged in Google Sheets to provide operational visibility.

Logs included:

- ticket ID  
- detected language  
- translation output  
- agent identifier  
- timestamp  

This created a record of automation performance and translation activity.

---

# Simulated Modern Implementation (Post-Integration)

A newer simulated version of this workflow was later built using the **native Zammad module available in Make.com**.

With recent improvements in Zammad and the availability of the direct integration, many processes that were previously handled in Make can now be managed **internally within Zammad itself**.

These include tasks such as:

- ticket tagging  
- business rule categorization  
- workflow triggers  
- automated responses  

As a result, the automation architecture becomes significantly simpler, with Make primarily responsible for orchestration and external services such as translation.

This demonstrates how automation systems evolve as platform integrations mature.

---

# Technology Stack

Legacy implementation:

- Make.com  
- OpenAI API  
- Zammad REST API (via HTTP module)  
- Google Sheets (logging)

Modern simulated implementation:

- Make.com  
- OpenAI API  
- Zammad native Make integration  

---

# Disclaimer

This repository contains a **reconstructed demonstration of automation concepts inspired by real-world implementations** that were originally developed for organizations under **Non-Disclosure Agreements (NDAs)**.

To honor those agreements, the workflows shown here do not replicate the exact production infrastructure, datasets, integrations, or operational environments used in the original systems. Instead, they illustrate the architectural approach using simplified logic and publicly available tools.

All examples in this repository are provided strictly for **portfolio and educational purposes**.
