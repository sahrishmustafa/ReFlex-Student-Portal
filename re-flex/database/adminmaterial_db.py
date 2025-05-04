import sqlite3

def save_file_to_db(material_type, file_content):
    """Save the uploaded file content to the SQLite database."""
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO AdminMaterial (type, file_content) 
    VALUES (?, ?)
    ''', (material_type, file_content))

    conn.commit()
    conn.close()