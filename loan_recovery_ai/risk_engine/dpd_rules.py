"""
dpd_rules.py
-----------------
RBI-aligned DPD (Days Past Due) classification logic
Used by Indian banks and NBFCs for asset classification
"""

def get_dpd_bucket(dpd: int) -> str:
    """
    Classify loan account based on RBI DPD norms
    
    Parameters:
    dpd (int): Days Past Due
    
    Returns:
    str: RBI DPD category
    """
    if dpd <= 30:
        return "Standard"
    elif dpd <= 60:
        return "SMA-1"
    elif dpd <= 90:
        return "SMA-2"
    else:
        return "NPA"


def get_risk_severity(dpd: int) -> str:
    """
    Map DPD to high-level risk severity
    Used by decision engine
    """
    if dpd <= 30:
        return "Low"
    elif dpd <= 60:
        return "Medium"
    elif dpd <= 90:
        return "High"
    else:
        return "Critical"


def dpd_summary(dpd: int) -> dict:
    """
    Returns a summary dictionary used in dashboards and decisions
    """
    return {
        "dpd": dpd,
        "dpd_bucket": get_dpd_bucket(dpd),
        "risk_severity": get_risk_severity(dpd)
    }
