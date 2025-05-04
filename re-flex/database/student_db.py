import sqlite3

def get_student_semester(student_email):
    # Returns the semester of a student based on their email.
    conn = sqlite3.connect('reflex.db') 
    cursor = conn.cursor()

    cursor.execute("SELECT semester FROM student WHERE email = ?", (student_email,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]  # Semester
    else:
        return None  # Student not found

def register_student_to_course(student_email, course_id, section_id):
    conn = sqlite3.connect('reflex.db')  # Update with your actual DB path
    cursor = conn.cursor()

    # Get student ID from email
    cursor.execute("SELECT id FROM Student WHERE email = ?", (student_email,))
    student_id = cursor.fetchone()[0]

    # Insert registration into Student_Course
    cursor.execute('''
        INSERT INTO Student_Course (studentid, courseid, sectionid)
        VALUES (?, ?, ?)
    ''', (student_id, course_id, section_id))

    conn.commit()
    conn.close()


def get_registered_courses_for_student(student_email):
    # Connect to the database
    conn = sqlite3.connect('reflex.db')  # Replace with your actual DB path
    cursor = conn.cursor()

    # Get student ID using the email
    cursor.execute("SELECT id FROM Student WHERE email = ?", (student_email,))
    student_id = cursor.fetchone()
    
    if student_id is None:
        return "Student not found."
    
    student_id = student_id[0]

    # Query to get registered courses for the student, joining with Course and Student_Course tables
    cursor.execute("""
        SELECT c.courseid, c.title, sc.sectionid
        FROM Student_Course sc
        JOIN Course c ON sc.courseid = c.courseid
        WHERE sc.studentid = ?
    """, (student_id,))
    
    courses = cursor.fetchall()

    conn.close()

    # Format the result into a table-like structure
    if courses:
        courses_list = [['Course Code', 'Course Title', 'Section']] + courses
        return courses_list
    else:
        return "No courses registered for this student."

def get_student_grades(student_email):
    conn = sqlite3.connect('reflex.db')  # Replace with your actual DB path
    cursor = conn.cursor()

    # Get student ID based on email
    cursor.execute("SELECT id FROM Student WHERE email = ?", (student_email,))
    student_id = cursor.fetchone()

    if not student_id:
        return "Student not found."

    student_id = student_id[0]

    # Get grades for the student
    cursor.execute(''' 
        SELECT course, type, total_marks, obtained_marks
        FROM Grades 
        WHERE studentid = ?
    ''', (student_id,))

    grades = cursor.fetchall()

    # Organize the results into the desired format
    result = [['Course', 'Assignment', 'Quiz', 'Midterm', 'Final']]
    
    courses = set([grade[0] for grade in grades])  # Unique courses
    for course in courses:
        # Initialize the grade row for each course
        row = [course, None, None, None, None]

        # Fill in the grades for each type (Assignment, Quiz, Midterm, Final)
        for grade in grades:
            if grade[0] == course:
                if grade[1] == 'Assignment':
                    row[1] = grade[3]
                elif grade[1] == 'Quiz':
                    row[2] = grade[3]
                elif grade[1] == 'Midterm':
                    row[3] = grade[3]
                elif grade[1] == 'Final':
                    row[4] = grade[3]

        result.append(row)

    conn.close()

    return result

def get_attendance_data(student_email):
    conn = sqlite3.connect('reflex.db') 
    cursor = conn.cursor()

    # Get student ID based on email
    cursor.execute("SELECT id FROM Student WHERE email = ?", (student_email,))
    student_id = cursor.fetchone()

    if not student_id:
        return "Student not found."

    student_id = student_id[0]

    # Get attendance data for the student
    cursor.execute(''' 
        SELECT course, section, COUNT(*) AS total_classes, 
               SUM(CASE WHEN status = 'Present' THEN 1 ELSE 0 END) AS attended
        FROM Attendance 
        WHERE studentid = ?
        GROUP BY course, section
    ''', (student_id,))

    attendance_data = cursor.fetchall()

    result = [['Course', 'Total Classes', 'Attended', 'Attendance %']]

    for data in attendance_data:
        course = data[0]
        total_classes = data[2]
        attended = data[3]
        attendance_percentage = (attended / total_classes) * 100
        result.append([course, total_classes, attended, f'{attendance_percentage:.2f}%'])

    conn.close()

    return result

def submit_feedback(user_email, feedback_text):
    # Just print to console for now (simulate storing it)
    print(f"Feedback received from {user_email}: {feedback_text}")


def get_academic_calendar():
    # Return a dummy academic calendar as text
    return (
        "📅 Academic Calendar 2024–2025\n\n"
        "- 🧑‍🏫 Semester 1: Aug 1 – Dec 15\n"
        "- 🧪 Midterms: Oct 10 – Oct 20\n"
        "- 🎄 Winter Break: Dec 16 – Jan 5\n"
        "- 📘 Semester 2: Jan 6 – May 10\n"
        "- 📝 Final Exams: May 1 – May 10"
    )


def drop_course(user_email, course_info):
    conn = sqlite3.connect('reflex.db')  # Connect to your database
    cursor = conn.cursor()
    
    # Step 1: Get student ID based on user email
    cursor.execute("SELECT id FROM Student WHERE email = ?", (user_email,))
    student = cursor.fetchone()

    course_id = course_info.split(" - ")[0]

    if student:
        student_id = student[0]
        
        # Step 2: Delete the course entry from Student_Course table
        cursor.execute("""
            DELETE FROM Student_Course
            WHERE studentid = ? AND courseid = ?
        """, (student_id, course_id))

        conn.commit()  
    else:
        print("Student not found.")

    conn.close()  # Close the connection