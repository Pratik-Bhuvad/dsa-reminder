from .connection import create_connection

def init_db():
    with create_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS problem_history (
                history_id INTEGER PRIMARY KEY AUTOINCREMENT,
                problem_id INTEGER NOT NULL,
                shown_at TEXT NOT NULL
            )
        """)