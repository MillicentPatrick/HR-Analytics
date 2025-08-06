# --- pages/diversity.py ---
import streamlit as st
import plotly.express as px
from utils.data_loader import load_employee_data
from utils.report_generator import generate_diversity_report

st.title("👥 Diversity & Inclusion Dashboard")
employee_data = load_employee_data()

# Gender breakdown
st.subheader("Gender Distribution")
if 'gender' in employee_data.columns:
    fig = px.pie(employee_data, names='gender', title="Gender Representation")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Gender data not available.")

# Ethnicity breakdown
st.subheader("Ethnicity Distribution")
if 'ethnicity' in employee_data.columns:
    fig = px.pie(employee_data, names='ethnicity', title="Ethnic Representation")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Ethnicity data not available.")

# Pay equity analysis
st.subheader("Pay Equity by Gender")
if 'gender' in employee_data.columns and 'salary' in employee_data.columns:
    fig = px.box(employee_data, x='gender', y='salary', title="Salary Distribution by Gender")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Gender or salary data not available.")

# Promotions by group (if available)
st.subheader("Promotion Analysis")
if 'promotion_date' in employee_data.columns:
    # Example - add more if you have detailed promotion info
    st.info("Detailed promotion tracking feature coming soon.")

# Diversity Recommendations
st.header("Recommendations for Inclusion")
st.markdown("""
- Improve outreach to underrepresented groups in hiring
- Conduct regular pay equity audits
- Encourage and fund employee resource groups (ERGs)
- Foster mentorship programs for minority talent
""")

# Download diversity report
st.subheader(" Download Diversity Report")
pdf = generate_diversity_report(employee_data)
st.download_button("Download PDF", data=pdf, file_name="diversity_report.pdf", mime="application/pdf")
