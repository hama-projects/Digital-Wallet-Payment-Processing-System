from backend.database.db import get_db_connection


def create_user(username: str, password: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id, username",
        (username, password),
    )

    user = cursor.fetchone()
    conn.commit()
    conn.close()

    return {"id": user[0], "username": user[1]}


def authenticate_user(username: str, password: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, username FROM users WHERE username=%s AND password=%s",
        (username, password),
    )

    user = cursor.fetchone()
    conn.close()

    if not user:
        return None

    return {"id": user[0], "username": user[1]}