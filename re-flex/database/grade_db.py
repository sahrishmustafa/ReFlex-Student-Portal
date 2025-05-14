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


def fetch_transcript(student_id):
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT course, section, type, total_marks, obtained_marks
        FROM Grades
        WHERE studentid = ?
    """, (student_id,))

    grades = cursor.fetchall()
    conn.close()

    transcript = {}
    for course, section, type_, total, obtained in grades:
        key = f"{course} (Sec {section})"
        if key not in transcript:
            transcript[key] = []
        transcript[key].append({
            'type': type_,
            'total': total,
            'obtained': obtained
        })
    return transcript
