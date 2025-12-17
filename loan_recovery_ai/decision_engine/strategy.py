"""
strategy.py
-----------------
Next-level collections decision engine for Indian banks/NBFCs

Features:
- RBI DPD-based escalation
- Risk-score based decisioning
- Expected recovery value optimisation
- Cost-aware collections strategy
"""

from risk_engine.dpd_rules import get_dpd_bucket, get_risk_severity

# --------------------------------------------------
# Recovery action configuration (India realistic)
# --------------------------------------------------

RECOVERY_ACTIONS = {
    "SMS_REMINDER": {
        "cost": 20,
        "base_success_prob": 0.20
    },
    "IVR_CALL": {
        "cost": 100,
        "base_success_prob": 0.35
    },
    "FIELD_VISIT": {
        "cost": 800,
        "base_success_prob": 0.60
    },
    "RESTRUCTURING": {
        "cost": 300,
        "base_success_prob": 0.55
    },
    "LEGAL_NOTICE": {
        "cost": 2000,
        "base_success_prob": 0.80
    }
}

# --------------------------------------------------
# Allowed actions by RBI risk severity
# --------------------------------------------------

ACTIONS_BY_SEVERITY = {
    "Low": ["SMS_REMINDER"],
    "Medium": ["SMS_REMINDER", "IVR_CALL"],
    "High": ["IVR_CALL", "FIELD_VISIT", "RESTRUCTURING"],
    "Critical": ["FIELD_VISIT", "LEGAL_NOTICE"]
}

# --------------------------------------------------
# Success probability adjustment using ML risk score
# --------------------------------------------------

def adjusted_success_probability(base_prob: float, risk_score: float) -> float:
    """
    Adjust action success probability based on ML risk score
    Higher risk -> lower recovery success
    """
    adjustment = 1 - (0.5 * risk_score)
    return max(0.05, min(base_prob * adjustment, 0.95))


# --------------------------------------------------
# Expected recovery calculation
# --------------------------------------------------

def expected_recovery_value(
    loan_amount: float,
    base_success_prob: float,
    risk_score: float,
    action_cost: float
) -> float:
    """
    Expected Recovery = (loan_amount * adjusted_prob) - cost
    """
    success_prob = adjusted_success_probability(base_success_prob, risk_score)
    return (loan_amount * success_prob) - action_cost


# --------------------------------------------------
# Main decision function
# --------------------------------------------------

def recommend_action(row) -> dict:
    """
    Recommend best recovery action for a loan account

    Expected columns in row:
    - loan_amount
    - dpd
    - risk_score
    """

    loan_amount = row["loan_amount"]
    dpd = row["dpd"]
    risk_score = row["risk_score"]

    dpd_bucket = get_dpd_bucket(dpd)
    risk_severity = get_risk_severity(dpd)

    possible_actions = ACTIONS_BY_SEVERITY[risk_severity]

    best_action = None
    best_value = float("-inf")

    for action in possible_actions:
        config = RECOVERY_ACTIONS[action]

        value = expected_recovery_value(
            loan_amount=loan_amount,
            base_success_prob=config["base_success_prob"],
            risk_score=risk_score,
            action_cost=config["cost"]
        )

        if value > best_value:
            best_value = value
            best_action = action

    return {
        "dpd_bucket": dpd_bucket,
        "risk_severity": risk_severity,
        "recommended_action": best_action,
        "expected_recovery_value": round(best_value, 2)
    }
