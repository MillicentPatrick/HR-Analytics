# --- pages/predictive_analytics.py ---
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_employee_data
from utils.report_generator import generate_predictive_report

st.title(" Predictive Attrition Analytics")

# Load data
df = load_employee_data()
df["engagement"] = df["engagement"].fillna(3)
df["performance"] = df["performance"].fillna(2)

# Predict attrition probability (simple formula)
df["attrition_probability"] = (
    0.65 - 0.2 * df["engagement"] + 0.1 * (3 - df["performance"])
).clip(0, 1)

#  Assign risk categories
def categorize_risk(prob):
    if prob > 0.7:
        return "High"
    elif prob > 0.4:
        return "Medium"
    else:
        return "Low"

df["risk_level"] = df["attrition_probability"].apply(categorize_risk)

#  Engagement vs Performance colored by risk
st.subheader("Engagement vs Performance by Risk Level")
fig = px.scatter(
    df,
    x="engagement",
    y="performance",
    color="risk_level",
    hover_data=["first_name", "last_name", "department", "attrition_probability"],
    title="Risk Categorization"
)
st.plotly_chart(fig, use_container_width=True)

#  Distribution of Predicted Attrition Probability
st.subheader("Attrition Probability Distribution")
fig = px.histogram(df, x="attrition_probability", nbins=20, color="risk_level", title="Probability Histogram")
st.plotly_chart(fig, use_container_width=True)

#  Threshold slider for custom view
st.subheader(" High Risk Employees")
threshold = st.slider("Set attrition probability threshold", 0.0, 1.0, 0.7)
high_risk = df[df["attrition_probability"] > threshold]

if high_risk.empty:
    st.info("No high-risk employees detected based on the current threshold.")
else:
    st.write(f"Employees with attrition probability > {threshold:.2f}")
    st.dataframe(high_risk[["first_name", "last_name", "department", "engagement", "performance", "attrition_probability"]])

#  Downloadable PDF Report
st.subheader(" Download Predictive Attrition Report")
pdf = generate_predictive_report(df)
st.download_button("Download PDF", data=pdf, file_name="predictive_attrition_report.pdf", mime="application/pdf")
