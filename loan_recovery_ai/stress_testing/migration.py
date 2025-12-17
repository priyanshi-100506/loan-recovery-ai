"""
migration.py
-----------------
DPD migration stress testing using transition matrices
Indian banking style delinquency modeling
"""

import numpy as np
import pandas as pd

DPD_STATES = ["Standard", "SMA-1", "SMA-2", "NPA"]

# -------------------------------
# Baseline transition matrix
# -------------------------------
BASE_TRANSITION_MATRIX = pd.DataFrame(
    [
        [0.90, 0.08, 0.01, 0.01],  # Standard
        [0.10, 0.70, 0.15, 0.05],  # SMA-1
        [0.05, 0.10, 0.65, 0.20],  # SMA-2
        [0.00, 0.00, 0.05, 0.95],  # NPA
    ],
    index=DPD_STATES,
    columns=DPD_STATES
)

# -------------------------------
# Stress transition matrix
# -------------------------------
STRESS_TRANSITION_MATRIX = pd.DataFrame(
    [
        [0.80, 0.15, 0.03, 0.02],
        [0.05, 0.60, 0.25, 0.10],
        [0.02, 0.08, 0.55, 0.35],
        [0.00, 0.00, 0.03, 0.97],
    ],
    index=DPD_STATES,
    columns=DPD_STATES
)

# -------------------------------
# Migration simulation
# -------------------------------
def simulate_dpd_migration(
    current_states: pd.Series,
    stressed: bool = False
) -> pd.Series:
    """
    Simulate next-period DPD state using transition matrix
    """
    matrix = STRESS_TRANSITION_MATRIX if stressed else BASE_TRANSITION_MATRIX

    next_states = []

    for state in current_states:
        probs = matrix.loc[state].values
        next_state = np.random.choice(DPD_STATES, p=probs)
        next_states.append(next_state)

    return pd.Series(next_states)
