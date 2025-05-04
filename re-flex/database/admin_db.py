import sqlite3

def get_admin_id_by_email(admin_email):
    # Connect to the SQLite database
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    # Query the database to get the faculty ID based on the email
    cursor.execute("SELECT id FROM Admin WHERE email = ?", (admin_email,))
    result = cursor.fetchone()

    conn.close()

    # If the faculty is found, return the faculty ID
    if result:
        return result[0]
    else:
        # If not found, return None or handle it as needed
        print("Admin email not found.")
        return None
