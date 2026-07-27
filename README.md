# High-Throughput ELK Workflow

Automates high-throughput ELK band structure calculations for multiple materials directly from CIF files using Python
---

## Overview
This project automates the  ELK workflow for multiple materials. It read multiple CIF files, generates ELK input file for each material, runs the calculations, and perform electronic band structure automatically.
---
## Features

- Read multiple CIF files
- Generate 'elk.in' automatically for each material
- Create separate calculation folders
- Run ELK SCF calculation
- Automate band structure calculations
- Batch processing for multiple materials
---

## Requirements

- Python 3.10+
- ELK
- pymatgen
---

## Workflow

```text
CIF Files
     │
     ▼
Read Crystal Structure
     │
     ▼
Generate elk.in
     │
     ▼
Run ELK
     │
     ▼
Ground-State Calculation
     │
     ▼
Band Structure Calculation
```

## Future Improvement

- Density of State (DOS) automation
- Phonon calculation
- Automatic k-point generation
- Automatic convergence calculations
