import sqlite3

def create_assignment_table(conn):
    # Create the table.
    conn.execute('''
    CREATE TABLE Assignment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        facultyid INTEGER,
        course TEXT,
        section TEXT,
        title TEXT,
        description TEXT,
        due_date DATE,
        file BLOB,
        FOREIGN KEY (facultyid) REFERENCES Faculty(id)
    );

    ''')

    with open('C:\\Users\\Hadi\\Downloads\\resume - hadiyatanveer.pdf', 'rb') as file:
        file_data = file.read()
        
    assignments = [
        (2, 'CS101', 'A', 'Assignment 1', 'Learn to make user stories.', '2025-05-10', file_data)
    ]
    conn.executemany('INSERT INTO Assignment (facultyid, course, section, title, description, due_date, file) VALUES (?, ?, ?, ?, ?, ?, ?)', assignments)