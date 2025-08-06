# --- pages/training.py ---
import streamlit as st
import plotly.express as px
from utils.data_loader import load_training_data
from utils.report_generator import generate_training_report

st.title("🎓 Training Effectiveness Dashboard")
training_data = load_training_data()

st.subheader("Training Completion Rates")
completion = training_data.groupby('course_name')['completion_date'].count().reset_index(name='completions')
fig = px.bar(completion, x='course_name', y='completions', title="Course Completions")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Skill Improvement")
training_data['improvement'] = training_data['post_test'] - training_data['pre_test']
fig = px.box(training_data, x='course_name', y='improvement', title="Skill Improvement by Course")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Application of Training")
applied_counts = training_data['applied'].value_counts().rename({1: 'Applied', 0: 'Not Applied'}).reset_index()
applied_counts.columns = ['Applied', 'Count']
fig = px.pie(applied_counts, names='Applied', values='Count', title="Training Application on the Job")
st.plotly_chart(fig, use_container_width=True)

st.subheader("📄 Download Training Report")
pdf = generate_training_report(training_data)
st.download_button("Download PDF", data=pdf, file_name="training_report.pdf", mime="application/pdf")
