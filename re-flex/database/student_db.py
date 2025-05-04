# database/student_db.py

from models.student import Student

def get_student_by_id(student_id):
    # Dummy hardcoded student
    return Student(student_id, "John Doe", "john@example.com")

def get_available_courses(student_email):
    # Return hardcoded available courses FOR THAT STUDENT
    return [
        {'id': 'CS101', 'name': 'Introduction to Computer Science'},
        {'id': 'MATH204', 'name': 'Linear Algebra'},
        {'id': 'PHY150', 'name': 'Mechanics and Waves'}
    ]

def get_registered_courses_for_student(student_email):
    # Dummy data for now
    return [
        ['Course Code', 'Course Title', 'Instructor', 'Section'],
        ['CS101', 'Introduction to Programming', 'Dr. Ahmed', 'A'],
        ['MATH201', 'Linear Algebra', 'Prof. Khan', 'B'],
        ['ENG301', 'Technical Writing', 'Ms. Sara', 'A'],
    ]

def get_student_grades(email):
    # Simulated dummy data for now
    return [
        ['Course', 'Assignment', 'Quiz', 'Midterm', 'Final', 'Total'],
        ['Data Structures', 85, 90, 78, 88, 85.25],
        ['Database Systems', 80, 85, 75, 90, 82.5],
        ['Software Engineering', 88, 87, 80, 85, 85.0]
    ]

def get_attendance_data(email):
    return [
        ['Course', 'Total Classes', 'Attended', 'Attendance %'],
        ['Data Structures', 30, 27, '90%'],
        ['Database Systems', 28, 25, '89.3%'],
        ['Software Engineering', 32, 29, '90.6%']
    ]

# database/student_db.py

def get_course_materials(user_email):
    # Return dummy course material data
    return [
        {
            'course': 'CS101',
            'filename': 'lecture1.pdf',
            'content': b'%PDF-1.4 Dummy content of PDF file for Lecture 1'
        },
        {
            'course': 'MA102',
            'filename': 'notes_week2.txt',
            'content': b'These are dummy notes for week 2.'
        }
    ]


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


def get_registered_courses(user_email):
    # Return dummy registered courses for testing drop functionality
    return [
        {'id': 'CS101', 'name': 'Introduction to Computer Science'},
        {'id': 'MA102', 'name': 'Calculus II'}
    ]


def drop_course(user_email, course_id):
    # Just print to console (simulate a delete operation)
    print(f"{user_email} dropped course {course_id}")
