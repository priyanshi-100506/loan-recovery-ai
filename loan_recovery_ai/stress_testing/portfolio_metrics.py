"""
portfolio_metrics.py
-----------------
Portfolio-level stress testing metrics
Used for management & RBI-style reporting
"""

import pandas as pd

def dpd_distribution(states: pd.Series) -> pd.DataFrame:
    """
    Calculate percentage distribution of DPD states
    """
    dist = states.value_counts(normalize=True) * 100
    return dist.round(2).to_frame(name="percentage")


def npa_ratio(states: pd.Series) -> float:
    """
    Percentage of portfolio in NPA
    """
    return round((states == "NPA").mean() * 100, 2)


def escalation_rate(
    current_states: pd.Series,
    next_states: pd.Series
) -> float:
    """
    % of loans that moved to worse DPD category
    """
    order = ["Standard", "SMA-1", "SMA-2", "NPA"]
    rank = {s: i for i, s in enumerate(order)}

    escalated = (
        next_states.map(rank).values >
        current_states.map(rank).values
    )

    return round(escalated.mean() * 100, 2)
