import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_employee_data
from utils.report_generator import generate_attrition_pdf, generate_attrition_csv

st.set_page_config(page_title="Attrition Analysis", layout="wide")
st.title(" Attrition Analysis")

employee_data = load_employee_data()

# Overall attrition metrics
col1, col2, col3 = st.columns(3)
with col1:
    total_employees = len(employee_data)
    st.metric("Total Employees", total_employees)
with col2:
    active_employees = employee_data['is_active'].sum()
    st.metric("Active Employees", active_employees)
with col3:
    attrition_rate = (1 - (active_employees / total_employees)) * 100 if total_employees > 0 else 0
    st.metric("Attrition Rate", f"{attrition_rate:.1f}%")

# Attrition trends over time
st.subheader(" Attrition Trends Over Time")
if 'hire_date' in employee_data.columns and 'termination_date' in employee_data.columns:
    employee_data['hire_year'] = pd.to_datetime(employee_data['hire_date']).dt.year
    employee_data['termination_year'] = pd.to_datetime(employee_data['termination_date']).dt.year

    attrition_yearly = employee_data[employee_data['termination_year'].notna()]
    attrition_yearly = attrition_yearly.groupby('termination_year').size().reset_index(name='Departures')

    fig = px.line(
        attrition_yearly,
        x='termination_year',
        y='Departures',
        title="Attrition Over Time",
        labels={'termination_year': 'Year', 'Departures': 'Number of Departures'}
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Date columns not available for trend analysis.")

# Attrition by department
st.subheader(" Attrition by Department")
if 'department' in employee_data.columns:
    departed = employee_data[employee_data['is_active'] == 0]
    attrition_by_dept = departed['department'].value_counts().reset_index()
    attrition_by_dept.columns = ['Department', 'Departures']

    fig = px.bar(
        attrition_by_dept,
        x='Department',
        y='Departures',
        title="Departures by Department"
    )
    st.plotly_chart(fig, use_container_width=True)

    dept_stats = employee_data.groupby('department').agg(
        total=('employee_id', 'count'),
        left=('is_active', lambda x: (x == 0).sum())
    ).reset_index()
    dept_stats['Attrition Rate (%)'] = (dept_stats['left'] / dept_stats['total']) * 100

    fig2 = px.bar(
        dept_stats,
        x='department',
        y='Attrition Rate (%)',
        title="Attrition Rate by Department (%)"
    )
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.warning("Department information not available.")

# Voluntary vs. Involuntary Turnover
st.subheader(" Voluntary vs. Involuntary Turnover")
if 'is_voluntary' in employee_data.columns:
    inactive_employees = employee_data[employee_data['is_active'] == 0]

    if not inactive_employees.empty:
        turnover_type = inactive_employees['is_voluntary'].value_counts()
        turnover_type.index = turnover_type.index.map({1: 'Voluntary', 0: 'Involuntary'})

        fig = px.pie(
            names=turnover_type.index,
            values=turnover_type.values,
            title="Voluntary vs Involuntary Turnover"
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No inactive employees to analyze turnover.")
else:
    st.warning("Turnover type data ('is_voluntary') not found.")

# Tenure analysis
st.subheader(" Tenure at Departure")
if 'tenure_days' in employee_data.columns:
    departed = employee_data[employee_data['is_active'] == 0]

    if not departed.empty:
        departed['tenure_years'] = departed['tenure_days'] / 365

        fig = px.histogram(
            departed,
            x='tenure_years',
            nbins=20,
            title="Distribution of Tenure at Departure (Years)",
            labels={'tenure_years': 'Tenure (Years)'}
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No departure data available for tenure analysis.")
else:
    st.warning("Tenure data not available.")

# Retention recommendations
st.header(" Retention Recommendations")
st.markdown("""
Based on yourthe attrition analysis, consider the following strategies:
- ** Exit Interviews**: Understand key reasons behind employee exits.
- ** Stay Interviews**: Proactively engage with current employees.
- ** Career Pathing**: Offer clear growth opportunities.
- ** Competitive Compensation**: Benchmark salaries regularly.
- ** Flexible Work**: Support hybrid or remote work options.
""")

# Download reports
st.subheader(" Download Reports")
col1, col2 = st.columns(2)
with col1:
    pdf = generate_attrition_pdf(employee_data)
    st.download_button("Download PDF Report", data=pdf, file_name="attrition_report.pdf", mime="application/pdf")

with col2:
    csv = generate_attrition_csv(employee_data)
    st.download_button("Download CSV Data", data=csv, file_name="attrition_data.csv", mime="text/csv")
