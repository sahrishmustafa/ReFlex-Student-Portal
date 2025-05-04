import sqlite3

def insert_assignment(facultyid, course, section, title, description, due_date, file_info):
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Assignment (facultyid, course, section, title, description, due_date, file)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (facultyid, course, section, title, description, due_date, file_info['content']))

    conn.commit()
    conn.close()
