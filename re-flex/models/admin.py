import sqlite3

def create_admin_table(conn):
    # Create the table.
    conn.execute('''
        CREATE TABLE IF NOT EXISTS Admin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')

    # Insert values. 
    conn.executemany('INSERT INTO Admin (name, email) VALUES (?, ?)', [
        ('Hadiya Tanveer', 'hadiyatanveer13@gmail.com'),
        ('Sahrish Mustafa', 'sahrish@example.com'),
        ('Maria Zahid', 'maria@example.com')
    ])
