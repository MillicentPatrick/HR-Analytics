# --- pages/user_management.py ---
import streamlit as st
import pandas as pd
from utils.data_loader import load_employee_data
from utils.report_generator import generate_user_management_report

st.title("👥 User Management")
employee_data = load_employee_data()

st.subheader("User Directory")
if not employee_data.empty:
    st.dataframe(
        employee_data[['employee_id', 'first_name', 'last_name', 'email', 'department', 'job_title', 'location', 'is_active']],
        use_container_width=True
    )

    st.subheader("Account Status Overview")
    status_counts = employee_data['is_active'].value_counts().rename({1: 'Active', 0: 'Inactive'}).reset_index()
    status_counts.columns = ['Status', 'Count']
    st.bar_chart(status_counts.set_index('Status'))

    st.subheader("Manage Users")
    selected_user = st.selectbox("Select Employee ID to View/Edit", employee_data['employee_id'])
    user_record = employee_data[employee_data['employee_id'] == selected_user].iloc[0]

    with st.form("edit_user_form"):
        new_email = st.text_input("Email", user_record['email'])
        new_status = st.selectbox("Status", options=['Active', 'Inactive'], index=0 if user_record['is_active'] else 1)
        submitted = st.form_submit_button("Update User")
        if submitted:
            st.success(f"User {selected_user} updated (not persisted in this demo).")
else:
    st.warning("No employee data available.")

st.subheader("📄 Download User Directory Report")
pdf = generate_user_management_report(employee_data)
st.download_button("Download PDF", data=pdf, file_name="user_management_report.pdf", mime="application/pdf")