import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    role TEXT
)
""")
conn.commit()


def add_user(user_id: int):
    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id, role) VALUES (?, ?)",
        (user_id, None)
    )
    conn.commit()


def set_role(user_id: int, role: str):
    cursor.execute(
        "UPDATE users SET role = ? WHERE user_id = ?",
        (role, user_id)
    )
    conn.commit()


def get_role(user_id: int):
    cursor.execute(
        "SELECT role FROM users WHERE user_id = ?",
        (user_id,)
    )
    row = cursor.fetchone()
    return row[0] if row else None


def clear_role(user_id: int):
    cursor.execute(
        "UPDATE users SET role = NULL WHERE user_id = ?",
        (user_id,)
    )
    conn.commit()
