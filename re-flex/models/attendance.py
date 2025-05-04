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
        date DATE, 
        status TEXT CHECK(status IN ('Present','Absent','Late')),
        FOREIGN KEY (facultyid) REFERENCES Faculty(id),
        FOREIGN KEY (studentid) REFERENCES Student(id)
    )
    ''')

    attendance = [
        (1, '22i-0977', 'CS101', 'A', '2024-05-04', 'Present'),
        (1, '22i-1033', 'CS101', 'A', '2024-05-04', 'Absent'),
        (1, '22i-1113', 'CS101', 'A', '2024-05-04', 'Late')
    ]
    
    conn.executemany('INSERT INTO Attendance (facultyid, studentid, course, section, date, status) VALUES (?, ?, ?, ?, ?, ?)', attendance)