# AI-Driven Cloud Security Framework for SME Healthcare  
_Reproducibility Package (Springer Discover Internet of Things, 2025 Revision)_

This repository contains the reproducibility materials for the paper:

> **AI-Driven Cloud Security Framework for SME Healthcare**  
> Authors: Yuanyuan Liu, Joel [Surname], Harrison [Surname], Weijun (Nick) Ma  
> Journal: *Springer Discover Internet of Things* (2025, in revision)

The repository provides code, sample data, figures, documentation, and environment configuration required to verify and reproduce the experiments described in the manuscript.

---

## 📁 Repository Structure

```text
.
├── README.md                     # Project overview (this file)
├── LICENSE                       # MIT license
├── environment.yml               # Conda environment configuration
├── requirements.txt              # Python dependencies
│
├── src/                          # Source code and scripts
│   ├── ai_intrusion_dashboard_refined.py
│   └── (additional scripts)
│
├── data/                         # Sample datasets (non-sensitive)
│   ├── attack_log_dataset.csv
│   └── README.md
│
├── results/
│   ├── figures/                  # All generated figures and plots
│   │   ├── Fig1_ai_workflow_diagram.png
│   │   ├── Fig2_experiment_environment_structure.png
│   │   ├── Fig3_system_architecture_diagram.png
│   │   ├── Fig4_system_data_flow.png
│   │   ├── Fig5_user_operation_flow.png
│   │   ├── Fig6_user_touch_points.png
│   │   ├── Fig7_performance_metrics_chart.png
│   │   ├── Fig8_non_it_user_metrics.png
│   │   ├── category_countplot.png
│   │   ├── incident_grade_piechart.png
│   │   ├── multiclass_roc_comparison.png
│   │   ├── attack_trend_over_time.png
│   │   └── (other figures)
│   └── README.md
│
└── docs/                         # Supplementary documents and artifacts
    ├── AI_Cloud_Security_Lab_Manual.docx
    ├── AI_Cloud_Security_Environment_Setup.docx
    ├── AI_Cloud_Security_Dashboard.md
    ├── AI_Cloud_Security_Lab_Experiment_Package.zip
    └── Automating_SIEM_Event_Management_with_Exp.pdf
