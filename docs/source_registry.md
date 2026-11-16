
# INTELLIQ — Data Source Registry

## 1. Purpose

This registry maintains a structured inventory of datasets
used by the INTELLIQ analytical platform.

Every dataset must have documented provenance, reporting
period, geographical coverage, measurement units and
verification status.

## 2. Sector Classification

| Sector ID | Sector |
|---|---|
| SEC-01 | Water |
| SEC-02 | Waste |
| SEC-03 | Energy |
| SEC-04 | Food & Agriculture |
| SEC-05 | Built Environment |
| SEC-06 | Advanced & Industrial Infrastructure |
| SEC-07 | Nature |
| SEC-08 | Mobility |

## 3. Dataset Master Registry

| Field | Description |
|---|---|
| Dataset ID | Unique dataset identifier |
| Sector ID | Associated sector |
| Dataset Name | Official dataset title |
| Publishing Organisation | Source organisation |
| Source URL | Original dataset URL |
| Data Format | CSV, XLSX, JSON, API, PDF |
| Geographic Coverage | National, state, district |
| Reporting Period | Monthly, quarterly, annual |
| Measurement Unit | MW, MLD, tonnes, etc. |
| Update Frequency | Expected update interval |
| Last Verified | Date of source verification |
| Access Method | API, download, scraping, manual |
| Verification Status | Pending, verified, rejected |
| Limitations | Known data limitations |

## 4. Initial Dataset Inventory

| Dataset ID | Sector | Dataset Name | Status |
|---|---|---|---|
| WAT-001 | Water | To be identified | Pending |
| WST-001 | Waste | To be identified | Pending |
| ENR-001 | Energy | To be identified | Pending |
| AGR-001 | Food & Agriculture | To be identified | Pending |
| BLD-001 | Built Environment | To be identified | Pending |
| IND-001 | Industrial Infrastructure | To be identified | Pending |
| NAT-001 | Nature | To be identified | Pending |
| MOB-001 | Mobility | To be identified | Pending |

## 5. Data Quality Standards

Every dataset must be assessed for:

1. Source authenticity
2. Completeness
3. Accuracy
4. Timeliness
5. Consistency
6. Geographic granularity
7. Unit standardisation
8. Historical availability

## 6. Data Provenance

Each ingested dataset should preserve:

- Original source URL
- Retrieval timestamp
- Original filename
- Reporting period
- Processing timestamp
- Transformation version
- Validation results

## 7. Verification Rules

- Official government sources receive priority.
- Secondary sources must be identified explicitly.
- Dataset URLs must be tested before being marked verified.
- Missing values must not be silently replaced.
- Conflicting figures must be documented.
- Historical revisions must be traceable.

## 8. Registry Status

Current status: Initial registry structure created.

No datasets have been marked as verified yet.
