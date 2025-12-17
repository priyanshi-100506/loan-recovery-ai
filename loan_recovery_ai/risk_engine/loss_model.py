"""
loss_model.py
-------------
Expected Loss (EL) computation
PD × LGD × EAD
"""

import pandas as pd

def assign_lgd(
    loan_amount: float,
    secured: bool = False
) -> float:
    """
    Simple LGD rules
    """
    if secured:
        return 0.4
    if loan_amount <= 100000:
        return 0.75
    return 0.65


def calculate_ead(loan_amount: float) -> float:
    """
    Exposure at Default (simplified)
    """
    return loan_amount


def expected_loss(
    pd_value: float,
    lgd: float,
    ead: float
) -> float:
    """
    EL = PD × LGD × EAD
    """
    return round(pd_value * lgd * ead, 2)
