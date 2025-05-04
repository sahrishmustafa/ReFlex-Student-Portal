import sqlite3

def create_student_table(conn):
    # Create the table.
    conn.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            semester INTEGER
        )
    ''')

    # Insert few examples. 
    conn.executemany('INSERT INTO Student (id, name, email, semester) VALUES (?, ?, ?, ?)', [
        ('22i-0977', 'Sahrish Mustafa', 'i220977@nu.edu.pk', 6),
        ('22i-1033', 'Maria Zahid', 'i221033@nu.edu.pk', 6),
        ('22i-1113', 'Hadiya Tanveer', 'i221113@nu.edu.pk', 6),
    ])
