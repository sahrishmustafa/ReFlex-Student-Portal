# ui/faculty_enter_grades.py

from pywebio.input    import select, input, NUMBER
from pywebio.output   import put_markdown, put_text, put_buttons, put_table, clear

# Dummy course→sections mapping
dummy_faculty_courses = {
    'CS101 - Intro to Programming': ['A', 'B'],
    'MATH201 - Calculus II':             ['A'],
    'ENG305 - Technical Writing':        ['A', 'C'],
}

# Dummy section-specific student emails
dummy_students = {
    'CS101 - Intro to Programming': {
        'A': ['alice@example.com','bob@example.com'],
        'B': ['charlie@example.com']
    },
    'MATH201 - Calculus II':             {'A': ['david@example.com','eva@example.com']},
    'ENG305 - Technical Writing':        {'A': ['frank@example.com'], 'C': ['grace@example.com','hannah@example.com']},
}

# In-memory grade store
GRADES = []


def handle_enter_grade(course, section, back_to_dashboard, user_email):
    """Prompt for one student’s grade under course/section, then confirm."""
    put_markdown(f"### ✏️ Enter Grades for {course} (Sec {section})")
    student_email = select('Student Email', dummy_students[course][section])
    grade_type    = select('Grade Type', ['Assignment', 'Quiz', 'Exam'])
    marks         = input('Marks (numeric)', type=NUMBER)

    # Save dummy with email tag
    GRADES.append({
        'course': course,
        'section': section,
        'student_email': student_email,
        'type': grade_type,
        'marks': marks,
        'entered_by': user_email
    })

    # Confirmation + back
    clear()
    put_text(f"✅ {user_email} recorded {marks} ({grade_type}) for {student_email} @ {course} (Sec {section})")
    put_buttons(
        ['🔙 Back to Grade Entry', '🏠 Back to Dashboard'],
        onclick=[
            lambda: enter_student_grades(back_to_dashboard, user_email),
            back_to_dashboard
        ]
    )


def enter_student_grades(back_to_dashboard, user_email):
    """Dashboard: list course×section with Enter buttons."""
    clear()
    put_markdown('# 📝 Enter Student Grades')
    rows = []
    for course, secs in dummy_faculty_courses.items():
        for sec in secs:
            rows.append([
                course,
                sec,
                put_buttons(
                    ['Enter'],
                    onclick=[
                        lambda c=course, s=sec: handle_enter_grade(c, s, back_to_dashboard, user_email)
                    ]
                )
            ])
    put_table([['Course', 'Section', 'Action'], *rows])
