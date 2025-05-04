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
