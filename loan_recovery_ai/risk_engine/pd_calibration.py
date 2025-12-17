"""
pd_calibration.py
-----------------
Convert risk score into Probability of Default (PD)
Explainable logistic calibration
"""

import numpy as np
import pandas as pd

def calibrate_pd(
    risk_score: pd.Series,
    k: float = 6.0,
    midpoint: float = 0.5
) -> pd.Series:
    """
    Convert risk score to Probability of Default (PD)
    
    Parameters:
    - k: sensitivity of curve
    - midpoint: score where PD ~ 50%
    """

    pd_values = 1 / (1 + np.exp(-k * (risk_score - midpoint)))

    return pd_values.round(4)
