import pandas as pd

# Paths to data
EMPLOYEE_DATA_PATH = "data/employee_data_pbi.csv"
TRAINING_DATA_PATH = "data/training_data_pbi.csv"
OPENINGS_DATA_PATH = "data/openings_data_pbi.csv"
APPLICATIONS_DATA_PATH = "data/applications_data_pbi.csv"

def load_employee_data():
    return pd.read_csv(EMPLOYEE_DATA_PATH, parse_dates=['hire_date', 'termination_date'], dayfirst=True)

def load_training_data():
    return pd.read_csv(TRAINING_DATA_PATH, parse_dates=['completion_date'], dayfirst=True)

def load_openings_data():
    return pd.read_csv(OPENINGS_DATA_PATH, parse_dates=['post_date', 'close_date'], dayfirst=True)

def load_applications_data():
    return pd.read_csv(APPLICATIONS_DATA_PATH, parse_dates=['application_date'], dayfirst=True)
