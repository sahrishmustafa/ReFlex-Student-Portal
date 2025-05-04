import sqlite3

def create_query_table(conn):
    # Create the table.
    conn.execute('''
    CREATE TABLE StudentQuery (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        facultyid INTEGER,
        studentid TEXT,
        courseid TEXT,
        sectionid TEXT,
        query TEXT,
        answer TEXT,
        FOREIGN KEY (facultyid) REFERENCES Faculty(id),
        FOREIGN KEY (studentid) REFERENCES Student(id),
        FOREIGN KEY (courseid) REFERENCES Course(courseid)
    )
    ''')

    # Insert the values. 
    queries = [
        (1, '22i-0977', 'CS101', 'A', 'When is the assignment due?'),
        (2, '22i-1033', 'CS101', 'A', 'Can I get feedback?'),
        (2, '22i-1113', 'CS101', 'A', 'Hey, will the project deadline get extended?')
    ]

    conn.executemany('INSERT INTO StudentQuery (facultyid, studentid, courseid, sectionid, query) VALUES (?, ?, ?, ?, ?)', queries)
