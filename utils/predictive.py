import pandas as pd
import numpy as np

def predict_attrition_risk(df):
    # Simple scoring for demo purposes — replace with a trained model
    df = df.copy()
    df['risk_score'] = np.random.rand(len(df))

    # Optionally, add rule-based modifiers
    df.loc[df['tenure_days'] < 365, 'risk_score'] += 0.2
    df.loc[df['engagement'] < 3, 'risk_score'] += 0.3
    df['risk_score'] = df['risk_score'].clip(0, 1)
    return df
