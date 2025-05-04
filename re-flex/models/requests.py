import sqlite3

def create_request_table(conn):
    # Create the table.
    conn.execute('''
    CREATE TABLE IF NOT EXISTS Requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        detail TEXT NOT NULL,
        action TEXT,
        notes TEXT
    )
    ''')

    # 2. Insert the requests
    requests_data = [
        ('Course Change', 'Switch CS101 to MATH201'),
        ('Exam Reschedule', 'Move ENG305 final to 2025-06-01')
    ]

    conn.executemany('''
        INSERT INTO Requests (type, detail)
        VALUES (?, ?)
    ''', requests_data)