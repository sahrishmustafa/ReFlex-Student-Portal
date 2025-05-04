import sqlite3

def insert_material(facultyid, course, section, title, description, file_info):
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Material (facultyid, course, section, title, description, file)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (facultyid, course, section, title, description, file_info['content']))

    conn.commit()
    conn.close()

def get_course_materials(registered_courses):
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    materials = []
    for course, _, section in registered_courses:
        cursor.execute('''
            SELECT course, title, file
            FROM Material
            WHERE course = ? AND section = ?
        ''', (course, section))

        rows = cursor.fetchall()
        for row in rows:
            materials.append({
                'course': row[0],
                'filename': row[1],
                'content': row[2]
            })

    conn.close()
    return materials

