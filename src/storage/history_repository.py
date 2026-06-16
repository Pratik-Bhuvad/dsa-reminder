from ..database.connection import create_connection

conn = create_connection()

def get_history():
    """Fetches the history of problems shown to the user from the database."""
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM problem_history")
        return cursor.fetchall()
    
def add_history(problem_id, shown_at):
    """Adds a new entry to the problem history in the database."""
    with conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO problem_history (problem_id, shown_at) VALUES (?, ?)", (problem_id, shown_at))
        conn.commit()
        
def clear_history():
    """Clears the entire problem history from the database."""
    with conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM problem_history")
        conn.commit()