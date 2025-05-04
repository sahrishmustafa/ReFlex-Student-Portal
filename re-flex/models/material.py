import sqlite3

def create_material_table(conn):
    # Create the table.
    conn.execute('''
    CREATE TABLE Material (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        facultyid INTEGER,
        course TEXT,
        section TEXT,
        title TEXT,
        description TEXT,
        file BLOB,
        FOREIGN KEY (facultyid) REFERENCES Faculty(id)
    );

    ''')

    with open('C:\\Users\\Hadi\\Downloads\\resume - hadiyatanveer.pdf', 'rb') as file:
        file_data = file.read()
        
    materials = [
        (2, 'CS101', 'A', 'Assignment 1 Guide', 'This is the reference material to understand the assignment 01.', file_data)
    ]
    
    conn.executemany('INSERT INTO Assignment (facultyid, course, section, title, description, file) VALUES (?, ?, ?, ?, ?, ?)', materials)