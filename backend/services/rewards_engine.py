from backend.database.db import get_db_connection


def get_user_points(user_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT points FROM rewards WHERE user_id=%s",
        (user_id,)
    )

    result = cursor.fetchone()
    conn.close()

    if not result:
        return 0

    return result[0]


def add_reward_points(user_id: int, points: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT points FROM rewards WHERE user_id=%s",
        (user_id,)
    )

    existing = cursor.fetchone()

    if existing:
        cursor.execute(
            "UPDATE rewards SET points = points + %s WHERE user_id=%s",
            (points, user_id)
        )
    else:
        cursor.execute(
            "INSERT INTO rewards (user_id, points) VALUES (%s, %s)",
            (user_id, points)
        )

    conn.commit()
    conn.close()

    return get_user_points(user_id)