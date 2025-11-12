AI-Driven Cloud Security Lab Dashboard - Setup & Usage Guide


Project Summary:
-------------------
This dashboard visualizes experimental results from the research paper:
"Adaptive AI-Driven Cloud Security: Automating SIEM Event Management and Enhancing Threat Detection with LLMs"

It simulates a practical AI-enhanced security monitoring and log analysis system for SMEs and healthcare environments.

Authors:
- Maxine Liu
- Harrison Bai
Course: JHU 605.731 | April 2025

-----------------------------------------------------------
 System Requirements:
-----------------------------------------------------------
- Python 3.8 or later
- pip (Python package installer)
- Internet connection to install dependencies

-----------------------------------------------------------
Step 1: Install Python
-----------------------------------------------------------
If not already installed, download Python from:
https://www.python.org/downloads/

Ensure you check the box "Add Python to PATH" during installation.

-----------------------------------------------------------
 Step 2: Set Up a Virtual Environment (Recommended)
-----------------------------------------------------------
Open Terminal (Mac/Linux) or Command Prompt (Windows) and run:

Windows:
> python -m venv venv
> venv\Scripts\activate

Mac/Linux:
$ python3 -m venv venv
$ source venv/bin/activate

-----------------------------------------------------------
 Step 3: Install Required Python Packages
-----------------------------------------------------------
Run the following command in your terminal:

pip install streamlit pandas plotly

To support the AI explainability and visuals used in the dashboard, also install:

pip install matplotlib

(You may also optionally install seaborn, though it's not required for this version.)

-----------------------------------------------------------
Step 4: Place Required Files Together
-----------------------------------------------------------
Ensure the following files are in the same folder:

- ai_intrusion_dashboard_refined.py
- attack_log_dataset.csv

-----------------------------------------------------------
 Step 5: Run the Dashboard
-----------------------------------------------------------
In the terminal, navigate to the folder where your files are saved and run:

streamlit run ai_intrusion_dashboard_refined.py

The dashboard will open in your default browser automatically at:
http://localhost:8501

-----------------------------------------------------------
Optional Notes:
-----------------------------------------------------------
- You can filter data using the sidebar controls.
- You can export filtered results as a CSV.
- AI explanations are simulated; GPT API integration can be added later.
- Do not rename the CSV file unless you update the script accordingly.

===========================================================
For questions or academic use, contact: yliu156@jhu.edu
===========================================================
