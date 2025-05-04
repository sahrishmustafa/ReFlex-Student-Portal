import sqlite3

def insert_request(studentid, request_type, detail):
    # Connect to the SQLite database
    conn = sqlite3.connect('reflex.db')  # Replace with your database path
    cursor = conn.cursor()

    # SQL query to insert a new request
    cursor.execute('''
        INSERT INTO Requests (studentid, type, detail)
        VALUES (?, ?, ?)
    ''', (studentid, request_type, detail))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

def get_students_request():
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, type, detail FROM Requests WHERE action IS NULL')
    rows = cursor.fetchall()

    REQUESTS = [{'id': row[0], 'type': row[1], 'detail': row[2]} for row in rows]

    conn.close()

    return REQUESTS

def update_request(request_id, action, note):
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    query = '''
        UPDATE Requests
        SET action = ?, notes = ?
        WHERE id = ?
    '''
    cursor.execute(query, (action, note, request_id))
    conn.commit()
    conn.close()