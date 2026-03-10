# Real Estate Submission Validation Automation (Immotool)

This project demonstrates an automated **real estate submission validation system** built using **Make.com**, **Google Drive**, **API-based document validation**, and **GoHighLevel (GHL)** as the CRM.

The workflow automatically processes property submissions, validates uploaded documents, applies acquisition business rules, and routes qualified leads to the acquisition team.

The system reduces manual document review and ensures that only valid property opportunities move forward in the acquisition pipeline.

---

# System Overview

Link: https://github.com/krsnp5/make_usecases/blob/main/object_validation/UC1_3_OV_Submissions.png

The automation acts as an **intake and validation layer** between property sellers and the internal acquisition team.

When a property owner submits documents, the system automatically:

1. Detects new document submissions
2. Extracts and analyzes property information
3. Validates document completeness and readability
4. Applies acquisition business rules
5. Updates the CRM pipeline accordingly
6. Triggers automated communications through GoHighLevel

GoHighLevel serves as the **single system of record** for all leads, validation results, and pipeline stages.

---

# Core Workflow

### 1. Submission Detection

The automation monitors a Google Drive submission folder.

When a new file or folder is uploaded, the workflow begins processing the submission.

Example submission documents may include:

- property documents
- energy certificates
- floor plans
- identification documents
- supporting attachments

---

### 2. CRM Lead Creation

Once a submission is detected, the automation creates or updates the lead inside **GoHighLevel**.

The workflow then creates a **new opportunity** in the acquisition pipeline so that the submission is immediately visible to the operations team.

CRM data stored includes:

- contact details
- property address
- submission source
- document links
- validation results

---

### 3. Document Extraction and Validation

Uploaded documents are downloaded and sent to an **API-based document processing service** through the Make HTTP module.

The system extracts relevant data such as:

- property type
- year built
- asking price
- document readability
- document completeness

The extracted information is normalized and stored as validation variables within the scenario.

---

### 4. Business Rule Validation

The system evaluates the property against acquisition rules.

Example validation rules include:

- Only **single-family homes** are accepted
- **Condos and commercial properties** are rejected
- Properties priced **above €200,000** are rejected
- Certain historic construction periods trigger **government escalation review**
- Submissions must include **complete and readable documents**

These rules determine how the opportunity is routed inside the CRM pipeline.

---

# Automated Routing Outcomes

After validation, the automation routes the opportunity into one of several CRM stages.

### Missing Documents

Triggered when required documents are not present.

Actions:

- Opportunity stage updated to **Missing Documents**
- Missing files recorded in CRM notes
- Follow-up communication handled by GHL automation

---

### Document Review Required

Triggered when documents are unreadable or incomplete.

Actions:

- Opportunity stage updated to **For Review**
- Internal notes added for lead manager
- Manual verification required

---

### Property Rejected

Triggered when the property fails acquisition criteria.

Examples:

- condo property type
- commercial property type
- price exceeds acquisition limit

Actions:

- Opportunity moved to **Rejected**
- rejection reason stored in CRM

---

### Government Escalation

Triggered when properties fall within specific historic construction periods that require special compliance handling.

Actions:

- Opportunity moved to **Government Escalation**
- internal notification triggered

---

### Qualified Acquisition Lead

Triggered when the submission passes all validation checks.

Conditions:

- documents complete
- documents readable
- single-family property
- price within acquisition threshold

Actions:

- Opportunity moved to **To Call**
- acquisition team notified
- follow-up communication initiated

---

# System Architecture

The automation is orchestrated using **Make.com** and structured around modular components.

Main modules include:

```
Google Drive – Watch Files
Google Drive – Resolve Submission Folder
Google Drive – Retrieve Submission Files
GoHighLevel – Create or Update Contact
GoHighLevel – Create Opportunity
HTTP – Document Extraction API
HTTP – Validation Engine
Tools – Normalize Validation Variables
Router – Business Rule Routing
GoHighLevel – Update Opportunity
```

All communications, notifications, and follow-up workflows are handled directly within **GoHighLevel automation sequences**.

---

# Technology Stack

- Make.com
- Google Drive
- HTTP APIs for document processing
- GoHighLevel CRM
- AI-powered document validation services

---

# Design Principles

This workflow was designed with the following goals:

- eliminate manual document triage
- enforce acquisition rules automatically
- centralize lead management in the CRM
- reduce operational bottlenecks
- create a scalable property intake pipeline

The system architecture ensures that only **validated acquisition opportunities reach the sales team**.

---

# Disclaimer

This repository contains a **simulated reconstruction of automation workflows inspired by real-world implementations** that were originally developed for organizations under **Non-Disclosure Agreements (NDAs)**.

To honor those agreements, the workflows, infrastructure, integrations, and datasets shown here differ from the original production environment.

The purpose of this repository is to demonstrate **automation architecture, workflow design, and system integration concepts** using publicly available tools.

All examples are provided strictly for **portfolio and educational purposes**.
