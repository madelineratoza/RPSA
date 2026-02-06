# Rehabilitation Provider Shortage Area (RPSA) Index Code

**Author:** Madeline Ratoza, PT, DPT, PhD
**Institution:** The University of St. Augustine for Health Sciences
**Status:** Research manuscript in review  

---

## Overview

This repository contains the analytic code used to construct and evaluate the **Rehabilitation Provider Shortage Area (RPSA) index**, a census-tract–level framework adapted from the federal Health Professional Shortage Area (HPSA) model.

The purpose of the RPSA framework is to support measurement of rehabilitation workforce need in a way that is transparent, reproducible, and compatible with policy applications.

This repository is provided to support **reproducibility and methodological transparency**.

---

## What This Code Does

The scripts in this repository support:

- Cleaning and harmonizing workforce and census data
- Constructing the RPSA index
- Assigning weighted shortage scores
- Running statistical validation analyses
- Supporting geospatial preparation workflows

---

## Data Availability

Raw provider data cannot be shared due to licensing and privacy restrictions.

To reproduce the full workflow, users must independently obtain:

- American Community Survey (ACS) census tract data
- CDC PLACES census tract dataset
- Public rehabilitation clinic location data
- State licensure data (via open records request)

Users are responsible for complying with all data-use agreements.

---

## Repository Structure

```
/code
    rpsa_analysis.R   # main workflow script
```

Additional documentation and scripts may be added as the project evolves.

---

## Reproducibility Statement

This repository reproduces the analytic framework described in the manuscript.  
Adaptation may be required for use in other geographic regions or updated datasets.

All scripts are annotated to indicate required inputs and expected outputs.

---

## Citation

If you use this code in academic work, please cite:

> Ratoza M et al. *Extending Federal Shortage Area Frameworks to the Rehabilitation Workforce: Addressing a Critical Measurement Gap.* Physical Therapy. (in review)

---

## Contact

For questions about the framework or code:

**Madeline Ratoza**  
The University of St. Augustine
mratoza@usa.edu


