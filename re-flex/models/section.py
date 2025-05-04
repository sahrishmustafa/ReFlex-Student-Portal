import sqlite3

def create_section_table(conn):
    # Create the table.
    conn.execute('''
    CREATE TABLE Section (
        sectionid TEXT,
        courseid TEXT,
        student_strength INTEGER,
        PRIMARY KEY (sectionid, courseid),
        FOREIGN KEY (courseid) REFERENCES Course(courseid)
    )
    ''')

    sections = [
        ('A', 'CS101', 25),
        ('B', 'MATH201', 30),
        ('B', 'CS101', 25),
    ]
    
    conn.executemany('INSERT INTO Section VALUES (?, ?, ?)', sections)