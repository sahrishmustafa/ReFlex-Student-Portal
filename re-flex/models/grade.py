import sqlite3

def create_grades_table(conn):
    # Create the table.
    conn.execute('''
    CREATE TABLE Grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        facultyid INTEGER,
        studentid TEXT,
        type TEXT,
        total_marks INTEGER,
        obtained_marks INTEGER,
        course TEXT,
        section TEXT,
        FOREIGN KEY (facultyid) REFERENCES Faculty(id),
        FOREIGN KEY (studentid) REFERENCES Student(id)
    )
    ''')

    # Insert the values. 
    grades = [
        (2, '22i-0977', 'Assignment', 100, 98, 'CS101', 'A'),
        (2, '22i-1033', 'Assignment', 100, 90, 'CS101', 'A'),
        (2, '22i-1113', 'Assignment', 100, 95, 'CS101', 'A')
    ]
    
    conn.executemany('INSERT INTO Grades (facultyid, studentid, type, total_marks, obtained_marks, course, section) VALUES (?, ?, ?, ?, ?, ?, ?)', grades)