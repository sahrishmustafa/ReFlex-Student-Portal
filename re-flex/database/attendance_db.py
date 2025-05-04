import sqlite3
from datetime import date

def insert_attendance(facultyid, studentid, course, section, date, status):
    # Connect to the SQLite database
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    # SQL query to insert a new attendance record
    query = '''
        INSERT INTO Attendance (facultyid, studentid, course, section, date, status)
        VALUES (?, ?, ?, ?, ?, ?)
    '''

    # Execute the query with the provided data
    cursor.execute(query, (facultyid, studentid, course, section, date, status))

    conn.commit()
    conn.close()
