
# -------------------------------------------------------------
# Streamlit Dashboard: Adaptive AI-Driven Cloud Security Lab
# Authors: Maxine Liu, Harrison Bai
# Purpose: Visualizing experimental results from AI-driven cloud security automation and SIEM log analysis
# -------------------------------------------------------------

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import random

# ---- Page Settings ----
st.set_page_config(layout="wide", page_title="AI-Driven Cloud Security Lab Dashboard")

# ---- Load Data ----
@st.cache_data
def load_data():
    attack_df = pd.read_csv("attack_log_dataset.csv", parse_dates=["timestamp"])
    return attack_df

df = load_data()

# ---- Simulate Country if not present ----
if 'country_code' not in df.columns:
    def simulate_country(ip):
        countries = ['US', 'CN', 'RU', 'DE', 'FR', 'IN', 'JP', 'KR', 'GB', 'BR', 'CA']
        weights = [0.2, 0.15, 0.1, 0.08, 0.08, 0.07, 0.07, 0.05, 0.05, 0.05, 0.05]
        return random.choices(countries, weights=weights)[0]
    df['country_code'] = df['source_ip'].apply(simulate_country)

# ---- Header Section ----
st.title("🛡️ AI-Driven Cloud Security Lab Dashboard")
st.markdown("""
This dashboard presents experimental results from the research paper:

### 🧾 *"Adaptive AI-Driven Cloud Security: Automating SIEM Event Management and Enhancing Threat Detection with LLMs"*

---

#### 📚 **What is this?**
A practical lab system that simulates and visualizes security logs from Microsoft Defender for Cloud, enhanced by Power Automate and LLM-inspired analytics.

#### 🧪 **What does it do?**
- Detects and visualizes simulated cyberattacks.
- Maps attack sources geographically.
- Shows attack trends over time.
- Simulates explainable AI-based log classification.

#### 🧠 **How can it be used?**
- As an educational security lab for non-cybersecurity professionals.
- To demonstrate low-code automation using Microsoft Azure + AI.
- To prototype future integration of GPT-based SIEM support.

#### ✍️ **Authors**  
Maxine Liu, Johns Hopkins University  
Harrison Bai, Johns Hopkins University

---
""")

# ---- Sidebar Filter ----
st.sidebar.title("🔎 Filter")
countries = st.sidebar.multiselect("Select Country", sorted(df['country_code'].unique()), default=df['country_code'].unique())
attack_types = st.sidebar.multiselect("Select Attack Type", sorted(df['attack_type'].unique()), default=df['attack_type'].unique())
severities = st.sidebar.multiselect("Select Severity", sorted(df['severity'].unique()), default=df['severity'].unique())

df_filtered = df[df['country_code'].isin(countries) & df['attack_type'].isin(attack_types) & df['severity'].isin(severities)]

# ---- Data Table Preview ----
st.subheader("📋 Filtered Intrusion Logs")
st.write(f"Total matching entries: {len(df_filtered)}")
st.dataframe(df_filtered.head(10), use_container_width=True)

# ---- Global Attack Map ----
st.subheader("🌍 Global Attack Origin Map")
country_counts = df_filtered['country_code'].value_counts().reset_index()
country_counts.columns = ['country', 'count']
fig_map = px.choropleth(country_counts, locations="country", locationmode="ISO-3",
                        color="count", color_continuous_scale="Reds",
                        title="Geographic Distribution of Intrusion Sources")
st.plotly_chart(fig_map, use_container_width=True)

# ---- Attack Trend Animation ----
st.subheader("📊 Animated Trend: Attack Types Over Time")
df_filtered['hour'] = df_filtered['timestamp'].dt.floor('H')
trend_data = df_filtered.groupby(['hour', 'attack_type']).size().reset_index(name='count')
fig_trend = px.bar(trend_data, x='attack_type', y='count', color='attack_type',
                   animation_frame=trend_data['hour'].dt.strftime('%Y-%m-%d %H:%M'),
                   range_y=[0, trend_data['count'].max() + 5])
st.plotly_chart(fig_trend, use_container_width=True)

# ---- Risk Severity Pie ----
st.subheader("🎯 Risk Level Distribution")
severity_counts = df_filtered['severity'].value_counts()
fig_pie = go.Figure(data=[go.Pie(labels=severity_counts.index, values=severity_counts.values, hole=0.4)])
fig_pie.update_traces(textinfo='percent+label')
st.plotly_chart(fig_pie, use_container_width=True)

# ---- Country Summary ----
st.subheader("🌐 Attack Summary by Country")
summary_table = df_filtered.groupby(['country_code', 'severity']).size().unstack(fill_value=0)
st.dataframe(summary_table, use_container_width=True)

# ---- Explainable AI Section ----
st.subheader("🧠 Explainable AI (Model Decision Explanation)")

selected_row = df_filtered.sample(1).iloc[0]
st.markdown(f"**Selected Event:** `{selected_row['attack_type']} from {selected_row['source_ip']}`")
st.markdown(f"**Predicted Risk Level:** `{selected_row['severity']}`")

st.markdown("##### 🧠 Model Explanation (Simulated)")
explanation = [
    "🔹 Based on IP reputation score.",
    "🔹 Known suspicious behavior pattern.",
    "🔹 High volume activity within short timeframe.",
    "🔹 Originates from high-risk country.",
    "🔹 Matches known threat signature database."
]
for line in explanation:
    st.markdown(line)

# ---- Export Button ----
st.subheader("📥 Export Filtered Data")
st.download_button("Download CSV", df_filtered.to_csv(index=False), "filtered_logs.csv", "text/csv")

# ---- Footer ----
st.markdown("___")
st.caption("Dashboard simulation built by Maxine Liu & Harrison Bai · JHU 605.731 Project · April 2025")
