import pandas as pd

def calculate_attrition_rate(df):
    total = len(df)
    active = df['is_active'].sum()
    return (1 - active / total) * 100 if total > 0 else 0

def format_salary(value):
    return "${:,.2f}".format(value)

def calculate_tenure(df):
    df['tenure_years'] = df['tenure_days'] / 365
    return df
