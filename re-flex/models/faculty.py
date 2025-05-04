import sqlite3

def create_faculty_table(conn):
    # Create the table.
    conn.execute('''
        CREATE TABLE Faculty (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')

    # Insert values. 
    conn.executemany('INSERT INTO Faculty (name, email) VALUES (?, ?)', [
        ('Dr. Javaria', 'javaria.zia@gmail.com'),
        ('Dr. Imran', 'imran.ashraf@gmail.com'),
        ('Mr. Hammad', 'hammad.majeed@gmail.com')
    ])
