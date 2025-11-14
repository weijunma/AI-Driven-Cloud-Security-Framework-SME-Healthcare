[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17605067.svg)](https://doi.org/10.5281/zenodo.17605067)


# AI-Driven Cloud Security Framework for SME Healthcare  
_Reproducibility Package (Springer Discover Internet of Things, 2025 Revision)_

This repository contains the reproducibility materials for the paper:

> **AI-Driven Cloud Security Framework for SME Healthcare**  
> Authors: Yuanyuan Liu, Joel Coffman, Harrison Bai, Weijun (Nick) Ma  
> Journal: *Springer Discover Internet of Things* (2025, in revision)

The repository provides code, sample data, figures, documentation, and environment configuration required to verify and reproduce the experiments described in the manuscript.

---

## 📌 Overview

This repository provides the reproducibility package for the AI-driven cloud security framework.  
The framework integrates:

- **Microsoft Defender for Cloud** and **Microsoft Sentinel** for security event detection and aggregation  
- **Azure Machine Learning** for risk classification and explainable AI  
- **Power Automate** for automated incident response  
- **Streamlit Dashboard** for visualization and user oversight

---

## 📁 Repository Structure

```text
.
├── README.md                     
├── LICENSE                       
├── environment.yml               
├── requirements.txt              
│
├── src/                          
│   ├── ai_intrusion_dashboard_refined.py
│   └── (additional scripts)
│
├── data/                         
│   ├── attack_log_dataset.csv
│   └── README.md
│
├── results/
│   ├── figures/                  
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
└── docs/                         
    ├── AI_Cloud_Security_Lab_Manual.docx
    ├── AI_Cloud_Security_Environment_Setup.docx
    ├── AI_Cloud_Security_Dashboard.md
    ├── AI_Cloud_Security_Lab_Experiment_Package.zip
    └── Automating_SIEM_Event_Management_with_Exp.pdf
```

---

## 🧪 Reproducibility Checklist

### **Environment Summary**
- Python **3.8**
- Scikit-learn **1.2**
- Tested on **Windows 10** / **Ubuntu 20.04**
- Dataset: **Synthetic subset** for reproducibility

---

### **Detailed Checklist**

| Component | Description |
|----------|-------------|
| Python Version | 3.8 |
| Required Libraries | Scikit-learn 1.2.0, Streamlit 1.5.0, Plotly 5.5.0 |
| Environment | Windows 10 / Ubuntu 20.04 |
| Dataset | Synthetic subset (anonymized attack & normal logs) |
| Models | Random Forest Classifier, XGBoost |
| Evaluation | Accuracy, Precision, Recall, F1-score |
| Response Time | ~300ms average |
| False Alarm Rate | 5.4% |

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/weijunma/AI-Driven-Cloud-Security-Framework-SME-Healthcare
cd AICloudSecurityFramework

# Install dependencies
pip install -r requirements.txt

# Run demo
streamlit run notebook_demo/experiment_demo.ipynb
```

---

## 📚 Citation

If you use this package, please cite:

```bibtex
@article{liu2025ai_cloud_security,
  title={An Adaptive, AI-Driven Cloud Security Framework Automating SIEM Event Management with Explainable AI},
  author={Liu, Yuanyuan and Bai, Harrison and Coffman, Joel and Ma, Weijun},
  journal={Discover Internet of Things},
  year={2025},
  publisher={Springer Nature}
}
```

---

## 📄 License
This repository is distributed under the MIT License.  
See `LICENSE` for details.

---

## 📬 Contact
For questions or support:

**Weijun Ma**  
📧 weijun.ma@ieee.org
