import sqlite3

def create_attendance_table(conn):
    # Create the table.
    conn.execute('''
    CREATE TABLE Attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        facultyid INTEGER,
        studentid TEXT,
        course TEXT,
        section TEXT,
        status TEXT CHECK(status IN ('P','A','L')),
        FOREIGN KEY (facultyid) REFERENCES Faculty(id),
        FOREIGN KEY (studentid) REFERENCES Student(id)
    )
    ''')

    attendance = [
        (1, '22i-0977', 'CS101', 'A', 'P'),
        (1, '22i-1033', 'CS101', 'A', 'A'),
        (1, '22i-1113', 'CS101', 'A', 'L')
    ]
    
    conn.executemany('INSERT INTO Attendance (facultyid, studentid, course, section, status) VALUES (?, ?, ?, ?, ?)', attendance)