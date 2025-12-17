"""
model.py
-----------------
Simple, explainable risk scoring model
Designed for Indian NBFC-style lending use cases
"""

import numpy as np

def predict_risk(df):
    """
    Predict risk score for each loan
    
    Expected columns:
    - loan_amount
    - monthly_income
    - emi
    - tenure_months
    - interest_rate
    """

    # Normalize features (simple, transparent)
    emi_income_ratio = df["emi"] / (df["monthly_income"] + 1)
    loan_size_factor = df["loan_amount"] / 1_000_000
    tenure_factor = df["tenure_months"] / 60
    interest_factor = df["interest_rate"] / 30

    # Weighted risk score (business-inspired)
    risk_score = (
        0.4 * emi_income_ratio +
        0.25 * loan_size_factor +
        0.2 * tenure_factor +
        0.15 * interest_factor
    )

    return np.clip(risk_score, 0, 1)
