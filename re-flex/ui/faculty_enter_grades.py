from pywebio.input    import select, input, NUMBER
from pywebio.output   import put_markdown, put_text, put_buttons, put_table, clear

# Dummy course→sections mapping
dummy_faculty_courses = {
    'CS101 - Intro to Programming': ['A', 'B'],
    'MATH201 - Calculus II':             ['A'],
    'ENG305 - Technical Writing':        ['A', 'C'],
}

# Dummy section-specific students
dummy_students = {
    'CS101 - Intro to Programming': {'A': ['Alice','Bob'], 'B': ['Charlie']},
    'MATH201 - Calculus II':             {'A': ['David','Eva']},
    'ENG305 - Technical Writing':        {'A': ['Frank'], 'C': ['Grace','Hannah']},
}

# In-memory grade store
GRADES = []


def handle_enter_grade(course, section, back_to_dashboard):
    """Prompt for one student’s grade under course/section, then confirm."""
    put_markdown(f"### ✏️ Enter Grades for {course} (Section {section})")
    student    = select('Student', dummy_students[course][section])
    grade_type = select('Grade Type', ['Assignment', 'Quiz', 'Exam'])
    marks      = input('Marks (numeric)', type=NUMBER)

    # Save dummy
    GRADES.append({
        'course': course,
        'section': section,
        'student': student,
        'type': grade_type,
        'marks': marks
    })

    # Confirmation + back
    clear()
    put_text(f"✅ Recorded {marks} ({grade_type}) for {student} @ {course} (Sec {section})")
    put_buttons(
        ['🔙 Back to Grade Entry', '🏠 Back to Dashboard'],
        onclick=[
            lambda: enter_student_grades(back_to_dashboard),
            back_to_dashboard
        ]
    )


def enter_student_grades(back_to_dashboard):
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
                        lambda c=course, s=sec: handle_enter_grade(c, s, back_to_dashboard)
                    ]
                )
            ])
    put_table([['Course', 'Section', 'Action'], *rows])
