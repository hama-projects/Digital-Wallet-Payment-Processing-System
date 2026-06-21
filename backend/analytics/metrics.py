from backend.database.db import get_db_connection


def transaction_success_rate():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM transactions")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM transactions WHERE status='SUCCESS'")
    success = cursor.fetchone()[0]

    conn.close()

    if total == 0:
        return 0

    return success / total


def average_transaction_value():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(amount) FROM transactions")
    result = cursor.fetchone()[0]

    conn.close()

    return float(result) if result else 0