import sqlite3

# Connect to database (or create if not exists)
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