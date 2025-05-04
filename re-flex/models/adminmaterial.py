import sqlite3

def create_adminmaterial_table(conn):
    # Create AdminMaterial table
    conn.execute('''
        CREATE TABLE AdminMaterial (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT CHECK(type IN ('Timetable', 'ExamSchedule')),
            file_content BLOB
        )
    ''')
    
