from backend.database.db import get_db_connection
from backend.services.fraud_detection import check_fraud
from backend.services.rewards_engine import add_reward_points


def process_payment(sender_id: int, receiver_id: int, amount: float):
    fraud_result = check_fraud(amount)

    if fraud_result["fraud_detected"]:
        return {
            "status": "FAILED",
            "reason": fraud_result["reason"]
        }

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT balance FROM wallets WHERE user_id=%s",
        (sender_id,)
    )
    sender_wallet = cursor.fetchone()

    if not sender_wallet or sender_wallet[0] < amount:
        conn.close()
        return {"status": "FAILED", "reason": "Insufficient balance"}

    cursor.execute(
        "UPDATE wallets SET balance = balance - %s WHERE user_id=%s",
        (amount, sender_id)
    )

    cursor.execute(
        "UPDATE wallets SET balance = balance + %s WHERE user_id=%s",
        (amount, receiver_id)
    )

    cursor.execute(
        "INSERT INTO transactions (sender_id, receiver_id, amount, status) VALUES (%s, %s, %s, %s)",
        (sender_id, receiver_id, amount, "SUCCESS")
    )

    conn.commit()
    conn.close()

    add_reward_points(sender_id, int(amount // 10))

    return {
        "status": "SUCCESS",
        "amount": amount
    }