"""
stress_el.py
------------
Stress-adjusted Expected Loss computation
"""

import pandas as pd
import numpy as np

def apply_pd_stress(
    pd_series: pd.Series,
    stress_factor: float = 1.5,
    cap: float = 0.95
) -> pd.Series:
    """
    Increase PD under stress
    """
    stressed_pd = pd_series * stress_factor
    return stressed_pd.clip(upper=cap).round(4)


def compute_stress_el(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Compute stressed Expected Loss
    """
    df = df.copy()
    df["pd_stress"] = apply_pd_stress(df["pd"])
    df["expected_loss_stress"] = (
        df["pd_stress"] * df["lgd"] * df["ead"]
    ).round(2)
    return df
