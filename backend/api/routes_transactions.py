from fastapi import APIRouter
from backend.services.payment_processor import process_payment

router = APIRouter()


@router.post("/transactions/send")
def send_payment(sender_id: int, receiver_id: int, amount: float):
    result = process_payment(sender_id, receiver_id, amount)
    return result


@router.get("/transactions/{user_id}")
def transaction_history(user_id: int):
    from backend.database.db import get_db_connection

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, sender_id, receiver_id, amount, status FROM transactions WHERE sender_id=%s OR receiver_id=%s",
        (user_id, user_id),
    )

    rows = cursor.fetchall()
    conn.close()

    transactions = []
    for r in rows:
        transactions.append(
            {
                "id": r[0],
                "sender_id": r[1],
                "receiver_id": r[2],
                "amount": float(r[3]),
                "status": r[4],
            }
        )

    return {"transactions": transactions}