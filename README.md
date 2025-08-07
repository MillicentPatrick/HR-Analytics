#  HR Analytics Dashboard

A data-driven HR dashboard built with **Streamlit** for analyzing:
- Employee attrition
- Diversity
- Engagement
- Training effectiveness
- Predictive analytics (attrition risk)
- Recruitment metrics
- User management

##  Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/MillicentPatrick/HR-analytics-project.git
   cd HR-analytics-project


 HR Analytics Project

A dynamic HR analytics dashboard that provides a 360° view into your workforce. It enables data-driven decisions across key areas like attrition, engagement, diversity, recruitment, performance, and predictive risk.

 Executive Summary

    Total Employees: 300

    Active Employees: 255

    Attrition Rate: 15.00%

    Average Tenure: 5.18 years

    Average Engagement: 3.18

    Average Performance Rating: 2.98

 Attrition Report

Visualize turnover trends and compare attrition rates across departments and time.

    Active vs. Exited employees

    Historical attrition trends

    Department-level attrition insights

 Diversity Report

Breakdown of employee representation across locations and departments:
Employees by Department:
Department	Count
Engineering	72
Operations	70
Sales	53
Marketing	42
HR	41
Finance	22
Employees by Location:
Location	Count
NYC	114
Chicago	98
Remote	59
Austin	29
📈 Engagement Report

Measure and track employee sentiment and motivation.

    Average Engagement Score: 3.18

    Engagement by Department:

Department	Avg Engagement
Engineering	3.24
Finance	3.14
HR	3.37
Marketing	3.17
Operations	3.00
Sales	3.21
🔮 Predictive Analytics

Proactively flag employees at risk of leaving using a heuristic model based on:

    Engagement

    Performance

    Tenure

Features:

    Risk scores (0–1 scale)

    Risk level classification (High / Medium / Low)

    Interactive visuals:

        Engagement vs. Performance (scatter)

        Risk distribution (bar)

    High-risk employee list

    Downloadable predictive report (PDF)

 Recruitment Report

Track hiring pipeline efficiency and outcomes.

    Total Applications: 1828

    Job Openings: 100

    Filled Positions: 73

 Training Report

The training module analyzes employee learning effectiveness.

**Key Metrics:**
- Total Trainings: 1301
- Avg Hours: 4.2 hrs
- Avg Skill Gain: 6.8
- Avg Test Score Gain: +8.3
- Courses Applied On Job: 67.1%
-Avg skill improvement :19.3
- Application  : 53.3%

**Most Popular Courses:**
- Conflict Resolution
- Python for beginners
- Workplace Safety
- Time Management
- Leadership 101
- Advanced Excel

All visuals and a downloadable PDF are available on the dashboard.



👥 User Management

View and manage all employees in a searchable and filterable list.
 Tech Stack

    Streamlit – Interactive UI

    Plotly – Visualizations

    Pandas – Data processing

    ReportLab / FPDF – PDF generation

    Modular design – Easily extensible

 Folder Structure

HR_Analytics_project/
│
├── pages/
│   ├── attrition.py
│   ├── engagement.py
│   ├── predictive_analytics.py
│   ├── recruitment.py
│   └── user_management.py
│
├── utils/
│   ├── data_loader.py
│   ├── report_generator.py
│   └── visualization_helpers.py
│
├── data/
│   └── employee_data.csv
│
├── README.md

└── app.py

👤 User Directory (Admin View)

Provides a secure, downloadable listing of all current employees, roles, departments, and status for internal audit or compliance.

📥 Deployment & Access

    🔗 Live Dashboard: https://hr-analytics-a7nokletpuvsu8yk8ri9pw.streamlit.app


