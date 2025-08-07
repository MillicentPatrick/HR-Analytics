import pandas as pd
import io
from utils.pdf_template import PDF


# -------------------- EXECUTIVE SUMMARY --------------------
def generate_summary_report(emp_df: pd.DataFrame) -> bytes:
    pdf = PDF()
    pdf.add_page()
    pdf.add_section_title("Executive Summary")

    total = len(emp_df)
    active = emp_df["is_active"].sum()
    rate = (1 - active / total) * 100 if total > 0 else 0
    avg_eng = emp_df["engagement"].mean()
    avg_tenure = emp_df["tenure_days"].mean() / 365

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, f"Total Employees: {total}", ln=True)
    pdf.cell(0, 10, f"Active Employees: {active}", ln=True)
    pdf.cell(0, 10, f"Attrition Rate: {rate:.2f}%", ln=True)
    pdf.cell(0, 10, f"Avg Engagement: {avg_eng:.2f}", ln=True)
    pdf.cell(0, 10, f"Avg Tenure (Years): {avg_tenure:.2f}", ln=True)

    output = io.BytesIO()
    pdf.output(output)
    return output.getvalue()


# -------------------- ATTRITION --------------------
def generate_attrition_pdf(df: pd.DataFrame) -> bytes:
    pdf = PDF()
    pdf.add_page()
    pdf.add_section_title("Attrition Report")

    total = len(df)
    total_left = df["is_active"].value_counts().get(False, 0)
    attrition_rate = (total_left / total * 100) if total > 0 else 0

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, f"Total Employees: {total}", ln=True)
    pdf.cell(0, 10, f"Employees Who Left: {total_left}", ln=True)
    pdf.cell(0, 10, f"Attrition Rate: {attrition_rate:.2f}%", ln=True)

    if "voluntary" in df.columns and not df[df["is_active"] == False].empty:
        voluntary_counts = df[df["is_active"] == False]["voluntary"].value_counts()
        voluntary = voluntary_counts.get(True, 0)
        involuntary = voluntary_counts.get(False, 0)
        pdf.cell(0, 10, f"Voluntary Attrition: {voluntary}", ln=True)
        pdf.cell(0, 10, f"Involuntary Attrition: {involuntary}", ln=True)
    else:
        pdf.cell(0, 10, "No attrition type breakdown available.", ln=True)

    output = io.BytesIO()
    pdf.output(output)
    return output.getvalue()


def generate_attrition_csv(df: pd.DataFrame) -> bytes:
    attrition_df = df[df["is_active"] == False]
    csv_data = attrition_df.to_csv(index=False).encode("utf-8")
    return csv_data


# -------------------- DIVERSITY --------------------
def generate_diversity_report(df: pd.DataFrame) -> bytes:
    pdf = PDF()
    pdf.add_page()
    pdf.add_section_title("Diversity Report")

    pdf.set_font("Arial", size=10)
    if "gender" in df.columns:
        gender_dist = df["gender"].value_counts(normalize=True) * 100
        pdf.cell(0, 10, "Gender Distribution:", ln=True)
        for gender, pct in gender_dist.items():
            pdf.cell(0, 10, f"{gender}: {pct:.1f}%", ln=True)
    else:
        pdf.cell(0, 10, "Gender data not available.", ln=True)

    pdf.ln(5)
    if "ethnicity" in df.columns:
        ethnicity_dist = df["ethnicity"].value_counts(normalize=True) * 100
        pdf.cell(0, 10, "Ethnicity Distribution:", ln=True)
        for eth, pct in ethnicity_dist.items():
            pdf.cell(0, 10, f"{eth}: {pct:.1f}%", ln=True)
    else:
        pdf.cell(0, 10, "Ethnicity data not available.", ln=True)

    output = io.BytesIO()
    pdf.output(output)
    return output.getvalue()


# -------------------- ENGAGEMENT --------------------
def generate_engagement_report(df: pd.DataFrame) -> bytes:
    pdf = PDF()
    pdf.add_page()
    pdf.add_section_title("Engagement Report")

    avg_eng = df["engagement"].mean()
    eng_by_dept = df.groupby("department")["engagement"].mean().sort_values(ascending=False)

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, f"Average Engagement Score: {avg_eng:.2f}", ln=True)
    pdf.ln(5)
    pdf.cell(0, 10, "Engagement by Department:", ln=True)

    for dept, score in eng_by_dept.items():
        pdf.cell(0, 10, f"{dept}: {score:.2f}", ln=True)

    output = io.BytesIO()
    pdf.output(output)
    return output.getvalue()


# -------------------- RECRUITMENT --------------------
def generate_recruitment_report(app_df: pd.DataFrame, open_df: pd.DataFrame) -> bytes:
    pdf = PDF()
    pdf.add_page()
    pdf.add_section_title("Recruitment Report")

    total_apps = len(app_df)
    total_openings = len(open_df)
    filled = open_df["filled"].sum()
    avg_days_to_fill = open_df["days_to_fill"].mean()

    source_dist = app_df["source"].value_counts()

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, f"Total Applications: {total_apps}", ln=True)
    pdf.cell(0, 10, f"Job Openings: {total_openings}", ln=True)
    pdf.cell(0, 10, f"Filled Positions: {filled}", ln=True)
    pdf.cell(0, 10, f"Avg Time to Fill (days): {avg_days_to_fill:.1f}", ln=True)

    pdf.ln(5)
    pdf.cell(0, 10, "Applications by Source:", ln=True)
    for source, count in source_dist.items():
        pdf.cell(0, 10, f"{source}: {count}", ln=True)

    output = io.BytesIO()
    pdf.output(output)
    return output.getvalue()


# -------------------- TRAINING --------------------
def generate_training_report(df: pd.DataFrame) -> bytes:
    pdf = PDF()
    pdf.add_page()
    pdf.add_section_title("Training Effectiveness Report")

    total_trainings = len(df)
    avg_hours = df["hours"].mean()
    avg_skill_gain = df["skill_improvement"].mean()
    applied_pct = df["applied"].mean() * 100
    avg_test_improvement = (df["post_test"] - df["pre_test"]).mean()

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, f"Total Trainings Conducted: {total_trainings}", ln=True)
    pdf.cell(0, 10, f"Average Training Hours: {avg_hours:.2f}", ln=True)
    pdf.cell(0, 10, f"Avg Pre/Post Test Score Gain: {avg_test_improvement:.2f}", ln=True)
    pdf.cell(0, 10, f"Avg Skill Improvement Score: {avg_skill_gain:.2f}", ln=True)
    pdf.cell(0, 10, f"Courses Applied On the Job: {applied_pct:.1f}%", ln=True)

    popular_courses = df["course_name"].value_counts().head(5)
    pdf.ln(8)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(0, 10, "Top 5 Most Attended Courses:", ln=True)
    pdf.set_font("Arial", size=10)
    for i, (course, count) in enumerate(popular_courses.items(), 1):
        pdf.cell(0, 10, f"{i}. {course}: {count} completions", ln=True)

    output = io.BytesIO()
    pdf.output(output)
    return output.getvalue()


# -------------------- PREDICTIVE  ANALYSIS --------------------
def generate_predictive_report(df: pd.DataFrame) -> bytes:
    pdf = PDF()
    pdf.add_page()
    pdf.add_section_title("Predictive Attrition Report")

    avg_prob = df["attrition_probability"].mean()
    high_risk_count = (df["attrition_probability"] > 0.7).sum()

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, f"Average Attrition Probability: {avg_prob:.2f}", ln=True)
    pdf.cell(0, 10, f"Employees at High Risk (> 0.7): {high_risk_count}", ln=True)

    top = df.sort_values("attrition_probability", ascending=False).head(10)
    pdf.ln(6)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(0, 10, "Top 10 Employees by Risk:", ln=True)
    pdf.set_font("Arial", size=10)

    for _, row in top.iterrows():
        pdf.cell(
            0, 10,
            f"{row.get('first_name', '')} {row.get('last_name', '')} | "
            f"Dept: {row.get('department', '')} | "
            f"Risk: {row['attrition_probability']:.2f}",
            ln=True
        )

    output = io.BytesIO()
    pdf.output(output)
    return output.getvalue()


# -------------------- USER MANAGEMENT --------------------
def generate_user_management_report(df: pd.DataFrame) -> bytes:
    pdf = PDF()
    pdf.add_page()
    pdf.add_section_title("User Directory Report")

    fields = ['employee_id', 'first_name', 'last_name', 'email', 'department', 'job_title', 'is_active']
    if all(col in df.columns for col in fields):
        user_df = df[fields].copy()
        user_df.columns = ['ID', 'First Name', 'Last Name', 'Email', 'Dept', 'Title', 'Active']
        pdf.add_table(user_df)
    else:
        pdf.set_font("Arial", size=10)
        pdf.cell(0, 10, "User data incomplete. Cannot generate directory.", ln=True)

    output = io.BytesIO()
    pdf.output(output)
    return output.getvalue()
