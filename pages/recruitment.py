# --- pages/recruitment.py ---
import streamlit as st
import plotly.express as px
from utils.data_loader import load_applications_data, load_openings_data
from utils.report_generator import generate_recruitment_report

st.title(" Recruitment Funnel Dashboard")
applications = load_applications_data()
openings = load_openings_data()

st.subheader("Applications by Stage")
stage_counts = applications['stage'].value_counts().reset_index()
stage_counts.columns = ['Stage', 'Count']
fig = px.bar(stage_counts, x='Stage', y='Count', title="Application Funnel")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Source Effectiveness")
source_counts = applications['source'].value_counts().reset_index()
source_counts.columns = ['Source', 'Count']
fig = px.pie(source_counts, names='Source', values='Count', title="Application Sources")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Time to Fill Roles")
fig = px.box(openings[openings['filled']], x='department', y='days_to_fill', title="Time to Fill by Department")
st.plotly_chart(fig, use_container_width=True)

st.subheader(" Download Recruitment Report")
pdf = generate_recruitment_report(applications, openings)
st.download_button("Download PDF", data=pdf, file_name="recruitment_report.pdf", mime="application/pdf")
