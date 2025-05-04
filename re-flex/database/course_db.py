import sqlite3

def get_faculty_courses_and_sections(facultyid):
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT 
        fc.courseid,
        c.title,
        fc.sectionid
        FROM Faculty_Course fc
        JOIN Course c ON fc.courseid = c.courseid
        JOIN Section s ON fc.courseid = s.courseid AND fc.sectionid = s.sectionid
        WHERE fc.facultyid = ?
    ''', (facultyid,))

    results = cursor.fetchall()

    # Format result as dictionary with course title as key and sections as list
    faculty_courses = {}

    for row in results:
        course_title = row[0]  # 'id' of the course
        section_id = row[2]    # 'sectionid'

        if course_title not in faculty_courses:
            faculty_courses[course_title] = []

        faculty_courses[course_title].append(section_id)

    conn.close()
    return faculty_courses

def get_students_in_sections(courseid):
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()

    query = '''
        SELECT 
            c.courseid AS course,
            sc.sectionid,
            s.id AS studentid
        FROM Student_Course sc
        JOIN Student s ON sc.studentid = s.id
        JOIN Course c ON sc.courseid = c.courseid
        WHERE sc.courseid = ?
    '''

    cursor.execute(query, (courseid,))
    results = cursor.fetchall()

    # Format result as dictionary with course titles and sections as nested dictionary
    students = {}

    for row in results:
        course_title = row[0]  # 'course' title
        section_id = row[1]    # 'sectionid'
        student_id = row[2]    # 'studentid'

        if course_title not in students:
            students[course_title] = {}

        if section_id not in students[course_title]:
            students[course_title][section_id] = []

        students[course_title][section_id].append(student_id)

    conn.close()
    return students

def insert_course(courseid, title, credithours, description, semester):
    conn = sqlite3.connect('reflex.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Course (courseid, title, credithours, description, semester)
        VALUES (?, ?, ?, ?, ?)
    ''', (courseid, title, credithours, description, semester))
    conn.commit()
    conn.close()

def get_available_courses_with_sections(semester):
    conn = sqlite3.connect('reflex.db')  # Replace with actual DB path
    cursor = conn.cursor()

    # Join Course and Section tables
    cursor.execute("""
        SELECT 
            Course.courseid, 
            Course.title, 
            Course.credithours, 
            Course.description,
            Section.sectionid, 
            Section.student_strength
        FROM Course
        JOIN Section ON Course.courseid = Section.courseid
        WHERE Course.semester = ?
    """, (semester,))

    results = cursor.fetchall()
    conn.close()

    return results