from backend.database.db import get_db_connection


def get_dashboard_summary():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM transactions")
    total_transactions = cursor.fetchone()[0]

    cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM transactions")
    total_volume = cursor.fetchone()[0]

    conn.close()

    return {
        "total_users": total_users,
        "total_transactions": total_transactions,
        "total_volume": float(total_volume),
    }