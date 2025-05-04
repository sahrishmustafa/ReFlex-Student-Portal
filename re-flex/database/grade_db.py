import sqlite3

def insert_grade(facultyid, course, section, studentid, type, total_marks, obtained_marks):
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Grades (facultyid, studentid, type, total_marks, obtained_marks, course, section)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (facultyid, studentid, type, total_marks, obtained_marks, course, section))

    conn.commit()
    conn.close()
