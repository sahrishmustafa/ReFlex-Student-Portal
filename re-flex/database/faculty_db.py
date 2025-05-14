import sqlite3

def get_faculty_id_by_email(faculty_email):
    # Connect to the SQLite database
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    # Query the database to get the faculty ID based on the email
    cursor.execute("SELECT id FROM Faculty WHERE email = ?", (faculty_email,))
    result = cursor.fetchone()

    conn.close()

    # If the faculty is found, return the faculty ID
    if result:
        return result[0]
    else:
        # If not found, return None or handle it as needed
        print("Faculty email not found.")
        return None
    

def get_faculty_by_course_section(courseid, sectionid):
    import sqlite3
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    query = '''
        SELECT F.id
        FROM Faculty F
        JOIN Faculty_Course FC ON F.id = FC.facultyid
        WHERE FC.courseid = ? AND FC.sectionid = ?;
    '''
    cursor.execute(query, (courseid, sectionid))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

