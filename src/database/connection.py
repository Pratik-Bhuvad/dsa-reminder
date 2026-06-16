import sqlite3 as sqlite

db_file = 'data/dsa_reminder.db'

def create_connection():
    """ create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite.connect(db_file)
        conn.row_factory = sqlite.Row
        return conn
    except sqlite.Error as e:
        print(e)

    return conn