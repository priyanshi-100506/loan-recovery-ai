"""
management_summary.py
---------------------
Executive summary for portfolio stress testing
"""

def generate_summary(
    baseline_el: float,
    stress_el: float,
    portfolio_size: int
) -> str:
    delta = stress_el - baseline_el
    pct_increase = (delta / baseline_el) * 100

    return f"""
PORTFOLIO STRESS TEST SUMMARY
----------------------------
Total Accounts: {portfolio_size}

Baseline Expected Loss : ₹{baseline_el:,.0f}
Stress Expected Loss   : ₹{stress_el:,.0f}
Incremental Loss       : ₹{delta:,.0f}

Stress Impact Increase : {pct_increase:.1f}%

KEY INSIGHT:
Economic stress materially increases portfolio risk,
requiring higher capital buffers and intensified recovery actions.
"""
