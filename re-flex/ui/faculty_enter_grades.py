from pywebio.input    import select, input, NUMBER
from pywebio.output   import put_markdown, put_text, put_buttons, put_table, clear

from database.course_db import get_faculty_courses_and_sections
from database.course_db import get_students_in_sections
from database.grade_db import insert_grade


def handle_enter_grade(course, section, back_to_dashboard, faculty_id):
    # Prompt for one student’s grade under course/section, then confirm.
    put_markdown(f"### ✏️ Enter Grades for {course} (Section {section})")
    
    STUDENTS = get_students_in_sections(course)
    
    student_id    = select('Student', STUDENTS[course][section])
    grade_type = select('Grade Type', ['Assignment', 'Quiz', 'Exam'])
    totalmarks = input('Total Marks (numeric)', type=NUMBER)
    marks      = input('Marks (numeric)', type=NUMBER)

    # Update the grades. 
    insert_grade(faculty_id, course, section, student_id, grade_type, totalmarks, marks)

    # Confirmation + back
    clear()
    put_text(f"✅ Recorded {marks} ({grade_type}) for {student_id} @ {course} (Sec {section})")
    put_buttons(
        ['🔙 Back to Grade Entry', '🏠 Back to Dashboard'],
        onclick=[
            lambda: enter_student_grades(back_to_dashboard, faculty_id),
            back_to_dashboard
        ]
    )


def enter_student_grades(back_to_dashboard, faculty_id):
    clear()
    put_markdown('# 📝 Enter Student Grades')

    faculty_courses = get_faculty_courses_and_sections(faculty_id)

    rows = []
    for course, secs in faculty_courses.items():
        for sec in secs:
            rows.append([
                course,
                sec,
                put_buttons(
                    ['Enter'],
                    onclick=[
                        lambda c=course, s=sec: handle_enter_grade(c, s, back_to_dashboard, faculty_id)
                    ]
                )
            ])
    put_table([['Course', 'Section', 'Action'], *rows])
