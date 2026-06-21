from backend.config import FRAUD_LIMIT


def check_fraud(amount: float):
    """
    Basic fraud rule:
    If transaction exceeds threshold -> flag
    """

    if amount > FRAUD_LIMIT:
        return {
            "fraud_detected": True,
            "reason": "Transaction exceeds allowed limit"
        }

    return {
        "fraud_detected": False
    }