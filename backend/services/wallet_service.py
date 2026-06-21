from backend.database.db import get_db_connection


def get_balance(user_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT balance FROM wallets WHERE user_id=%s",
        (user_id,)
    )

    result = cursor.fetchone()
    conn.close()

    if not result:
        return 0

    return float(result[0])


def deposit_money(user_id: int, amount: float):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT balance FROM wallets WHERE user_id=%s",
        (user_id,)
    )

    wallet = cursor.fetchone()

    if wallet:
        cursor.execute(
            "UPDATE wallets SET balance = balance + %s WHERE user_id=%s",
            (amount, user_id)
        )
    else:
        cursor.execute(
            "INSERT INTO wallets (user_id, balance) VALUES (%s, %s)",
            (user_id, amount)
        )

    conn.commit()
    conn.close()

    return get_balance(user_id)