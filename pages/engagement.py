# --- pages/engagement.py ---
import streamlit as st
import plotly.express as px
from utils.data_loader import load_employee_data
from utils.report_generator import generate_engagement_report

st.title(" Employee Engagement Dashboard")
employee_data = load_employee_data()

# Engagement Overview
st.subheader("Engagement Scores Distribution")
if 'engagement' in employee_data.columns:
    fig = px.histogram(employee_data, x='engagement', nbins=10, title="Employee Engagement Histogram")
    st.plotly_chart(fig, use_container_width=True)

    engagement_avg = employee_data['engagement'].mean()
    st.metric("Average Engagement Score", f"{engagement_avg:.2f}")
else:
    st.warning("Engagement data not available.")

# Correlation with Retention
st.subheader("Engagement vs Retention")
if 'engagement' in employee_data.columns and 'is_active' in employee_data.columns:
    retention_group = employee_data.groupby('engagement')['is_active'].mean().reset_index()
    fig = px.line(retention_group, x='engagement', y='is_active', labels={'is_active': 'Retention Rate'},
                  title="Retention Rate by Engagement Score")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Insufficient data for engagement-retention correlation.")

# Recommendations
st.header("Strategies to Improve Engagement")
st.markdown("""
- Conduct regular pulse surveys and feedback sessions
- Recognize and reward employee contributions
- Encourage work-life balance and flexibility
- Foster a transparent and communicative work environment
""")

# Download engagement report
st.subheader(" Download Engagement Report")
pdf = generate_engagement_report(employee_data)
st.download_button("Download PDF", data=pdf, file_name="engagement_report.pdf", mime="application/pdf")
