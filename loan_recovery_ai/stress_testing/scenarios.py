"""
scenarios.py
-----------------
Stress testing scenarios for loan recovery system
Indian NBFC-style shock simulations
"""

import pandas as pd

def income_shock(df, shock_pct: float):
    """
    Simulate income drop (e.g., 20% salary cut)
    """
    stressed_df = df.copy()
    stressed_df["monthly_income"] = stressed_df["monthly_income"] * (1 - shock_pct)
    return stressed_df


def emi_shock(df, shock_pct: float):
    """
    Simulate EMI increase (e.g., rate hike)
    """
    stressed_df = df.copy()
    stressed_df["emi"] = stressed_df["emi"] * (1 + shock_pct)
    return stressed_df


def combined_shock(df, income_drop_pct: float, emi_rise_pct: float):
    """
    Combined stress: income drop + EMI rise
    """
    stressed_df = df.copy()
    stressed_df["monthly_income"] *= (1 - income_drop_pct)
    stressed_df["emi"] *= (1 + emi_rise_pct)
    return stressed_df
