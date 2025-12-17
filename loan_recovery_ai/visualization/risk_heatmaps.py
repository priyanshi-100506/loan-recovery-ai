"""
risk_heatmaps.py
----------------
Risk concentration heatmaps
"""

import pandas as pd
import matplotlib.pyplot as plt

def loan_dpd_heatmap(df: pd.DataFrame):
    df = df.copy()

    df["loan_bucket"] = pd.cut(
        df["loan_amount"],
        bins=[0, 100000, 300000, 1000000],
        labels=["Small", "Medium", "Large"]
    )

    pivot = pd.pivot_table(
        df,
        values="expected_loss_stress",
        index="loan_bucket",
        columns="dpd",
        aggfunc="sum",
        fill_value=0
    )

    plt.figure()
    plt.imshow(pivot)
    plt.colorbar(label="₹ Stress Expected Loss")
    plt.xticks(range(len(pivot.columns)), pivot.columns)
    plt.yticks(range(len(pivot.index)), pivot.index)
    plt.title("Stress EL Heatmap: Loan Size vs DPD")
    plt.show()
