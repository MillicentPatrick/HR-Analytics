# --- pages/home.py ---
import streamlit as st
from utils.data_loader import load_employee_data
from utils.report_generator import generate_summary_report

st.set_page_config(page_title="PeoplePulse HR Dashboard", layout="wide")
st.title(" PeoplePulse HR Dashboard - Home")

employee_data = load_employee_data()
total_employees = len(employee_data)
active_employees = employee_data['is_active'].sum()
attrition_rate = (1 - (active_employees / total_employees)) * 100 if total_employees > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Employees", total_employees)
col2.metric("Active Employees", active_employees)
col3.metric("Attrition Rate", f"{attrition_rate:.1f}%")

st.markdown("---")
st.header(" Quick Navigation")

with st.expander(" Navigate to Modules", expanded=True):
    st.page_link("pages/attrition.py", label=" Attrition Analysis")
    st.page_link("pages/diversity.py", label=" Diversity Dashboard")
    st.page_link("pages/engagement.py", label=" Engagement Insights")
    st.page_link("pages/predictive_analytics.py", label="🔮 Predictive Analytics")
    st.page_link("pages/recruitment.py", label=" Recruitment Metrics")
    st.page_link("pages/training.py", label="🎓 Training Effectiveness")
    st.page_link("pages/user_management.py", label="👥 User Management")

st.markdown("---")
st.subheader(" Download Executive Summary Report")
pdf = generate_summary_report(employee_data)
st.download_button("Download PDF Summary", data=pdf, file_name="executive_summary_report.pdf", mime="application/pdf")