
import matplotlib.pyplot as plt
import pandas as pd

def plot_el_comparison(baseline_el, stress_el):
    labels = ["Baseline EL", "Stress EL"]
    values = [baseline_el, stress_el]

    plt.figure()
    plt.bar(labels, values)
    plt.title("Expected Loss: Baseline vs Stress")
    plt.ylabel("₹ Loss")
    plt.show()

def plot_pd_distribution(df):
    plt.figure()
    plt.hist(df["pd"], bins=20, alpha=0.6, label="Baseline PD")
    plt.hist(df["pd_stress"], bins=20, alpha=0.6, label="Stress PD")
    plt.legend()
    plt.title("PD Distribution")
    plt.xlabel("Probability of Default")
    plt.ylabel("Count")
    plt.show()
