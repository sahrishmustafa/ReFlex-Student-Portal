import sqlite3

def get_student_queries_for_faculty(facultyid):
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT 
        sq.id,
        sq.courseid,
        sq.sectionid AS section,
        s.name AS student,
        sq.query
        FROM StudentQuery sq
        JOIN Student s ON sq.studentid = s.id
        WHERE sq.facultyid = ? AND (sq.answer IS NULL OR TRIM(sq.answer) = '')
    ''', (facultyid, ))

    results = cursor.fetchall()
    conn.close()

    STUDENT_QUERIES = [
        {'id': row[0], 'course': row[1], 'section': row[2], 'student': row[3], 'query': row[4]}
        for row in results
    ]

    return STUDENT_QUERIES

def update_student_query_answer(query_id, answer):
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE StudentQuery
        SET answer = ?
        WHERE id = ?
    ''', (answer, query_id))

    conn.commit()
    conn.close()
