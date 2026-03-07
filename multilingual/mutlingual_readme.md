## Multilingual Customer Support Automation (Make.com + Zammad + OpenAI)

This project demonstrates a multilingual customer support automation workflow built using **Make.com**, **OpenAI**, and **Zammad**.

The goal of the system is to allow a **German-speaking support team** to communicate seamlessly with customers who write in **any language**, without requiring agents to speak multiple languages.

The workflow uses AI translation and automation to bridge the communication gap between customers and support agents.

---

## System Overview

The automation consists of **three primary use cases**:

1. Use Case 1: Inbound Ticket Translation
Scenario: https://github.com/krsnp5/make_usecases/blob/main/multilingual/UC1_Inbound_Ticket_Translation.png

Customer messages written in any language are automatically detected and translated into German for the support team. The original language is also stored on the ticket so future responses can be translated back to the customer's native language.

2. Use Case 2: Automated SLA Response
Scenario: https://github.com/krsnp5/make_usecases/blob/main/multilingual/UC2_Automated_SLA_Response.png

When a new customer message is received, the system automatically sends an acknowledgement in the customer's original language confirming receipt of the request and expected response time. Safeguards ensure the SLA message is only sent once per ticket.

3. Use Case 3: Outbound Response Translation 
Scenario: https://github.com/krsnp5/make_usecases/blob/main/multilingual/UC3_Outbound_Message_Translation.png

Support agents respond internally in German. The system automatically translates the reply into the customer's original language before sending it. This allows agents to work in one internal language while supporting customers globally.

Together, these workflows create a **translation bridge** between customers and the internal support team.
