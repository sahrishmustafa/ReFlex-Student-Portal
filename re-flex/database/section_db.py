import sqlite3

def insert_section(sectionid, courseid, student_strength):
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO Section (sectionid, courseid, student_strength)
        VALUES (?, ?, ?)""", (sectionid, courseid, student_strength))
    conn.commit()
    conn.close()