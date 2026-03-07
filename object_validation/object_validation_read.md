# Real Estate Due Diligence Checker (Make.com + Google Drive + Google Document AI + GHL)

This project demonstrates a document intake and due diligence automation workflow built using **Make.com**, **Google Drive**, **Google Document AI**, **GHL**, and email automation.

The goal of the system is to help a real estate team review client-submitted property documents faster by validating file quality, document completeness, and property fit before a human follow-up takes place.

The workflow combines **document extraction**, **rule-based validation**, and **automated routing** to support a more efficient due diligence process.

---

## System Overview

The automation is designed around document submissions uploaded by clients into **Google Drive**.

Once files are uploaded, the system evaluates:

- whether the documents are readable
- whether the required files are complete
- whether the property fits the company's acquisition criteria
- whether the case should be rejected, escalated, or routed for follow-up

---

## Scenario

https://github.com/krsnp5/make_usecases/blob/main/object_validation/UC1-3_OV_Submissions.png

## Use Cases

### 1. Document Readability and Completeness Check
When a client uploads documents to Google Drive, the system scans the files using Google Document AI to assess readability and completeness. Illegible or incomplete submissions are flagged for manual review or follow-up.

### 2. Real Estate Object Validation
The system checks whether the submitted property matches predefined acquisition criteria. Invalid property types such as condos or commercial spaces are rejected, while restricted-property cases are escalated for management review.

### 3. Acquisition Routing and Client Communication
If the documents are readable, complete, and the property meets business rules, the case is routed to the Acquisition Manager in GHL with a “To Call” status. The client also receives an acknowledgement email with the expected callback timeline.

---

## Validation Rules

The workflow is designed to support checks such as:

- required documents submitted
- readable and legible files
- single-family homes only
- no condos
- no commercial spaces
- reject properties below **€200,000**
- escalate properties that fall under restricted or special historical-era criteria
- assign manual review if document quality is too poor for automated processing

---

## Example Outcomes

### A. Illegible Files
If uploaded files are unreadable or low quality:

- assign task to **Lead Manager**
- set GHL status to **For Review**

### B. Complete and Qualified Submission
If documents are complete, readable, and the property passes the business rules:

- assign task to **Acquisition Manager**
- set GHL status to **To Call**
- send acknowledgement email:

> Thanks for submitting your documents. Our real estate team is reviewing them at the moment and will give you a call within 2–3 business days.

### C. Incomplete Submission
If required documents are missing:

- send automatic email requesting missing files
- optionally route the case for follow-up

### D. Rejected or Escalated Property
If the property fails core acquisition rules or matches a restricted special-case category:

- reject automatically or
- escalate to the appropriate manager for review

## Workflow Behavior

Every time a client uploads a document into the designated Google Drive submission folder, the automation will automatically create a **GHL task** representing that submission.

This task becomes the central record for the case and will be updated as the automation performs validation checks.

The workflow then evaluates the uploaded files and updates the GHL task accordingly based on the validation results.

---

## Task Routing Logic

Once a submission is detected and a GHL task is created, the system evaluates the uploaded documents and applies the following logic:

### Illegible Files
If the uploaded documents are unreadable or too low quality for automated processing:

- GHL task is assigned to **Lead Manager**
- Status is set to **For Review**

### Incomplete Submission
If required documents are missing:

- Client receives an automated email requesting the missing files
- GHL task status may be set to **Missing Documents**

### Qualified Submission
If the documents are readable, complete, and the property meets acquisition criteria:

- GHL task is assigned to **Acquisition Manager**
- Status is set to **To Call**
- Client receives a confirmation email:

> Thanks for submitting your documents. Our real estate team is reviewing them at the moment and will give you a call within 2–3 business days.

### Rejected or Escalated Property
If the property fails acquisition criteria (for example property value below €200,000 or disallowed property types):

- the GHL task is either **rejected** automatically or
- **escalated to management** for review

## Disclaimer

The workflow presented in this project is a **simulated reconstruction of production-style automation** originally developed for companies and clients under **Non-Disclosure Agreements (NDAs)**.

To respect those agreements, the implementation shown here does **not reflect the exact production systems, infrastructure, datasets, or configurations** used in the original environments.

Instead, the scenarios in this repository recreate the **same architectural concepts and automation logic** using publicly available tools, sandbox environments, and mock data. Certain business rules, integrations, and technical details may differ from the original implementations to ensure that no confidential or proprietary information is disclosed.

These examples are intended strictly for **portfolio and demonstration purposes**.
