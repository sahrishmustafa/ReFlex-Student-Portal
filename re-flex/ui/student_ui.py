from pywebio.output import put_buttons, put_markdown, clear

def student_dashboard(user_email):
    # Import use case modules here (one per page)
    from ui import student_course_registration, student_view_courses, student_view_grades
    from ui import student_view_attendance, student_apply_scholarship, student_submit_assignment
    from ui import student_download_material, student_give_feedback, student_view_calendar
    from ui import student_communicateteachers, student_apply_leaves, student_view_transcript
    from ui import student_drop_course, student_view_exam_schedule

    clear()
    put_markdown(f"# 🎓 Student Dashboard ({user_email})")

    put_buttons(
        [
             'Register Courses', 'View Registered Courses', 'View Grades',
             'Attendance Record', 'Scholarships & Aid', 'Submit Assignment',
             'Download Materials', 'Give Feedback', 'Academic Calendar',
             'Drop Courses', 'Communicate with Teahcer', 'Apply for Leave', 'View Transcript',
             'View Exam Schedule'
        ],
        onclick=[
            lambda: student_course_registration.course_registration(user_email, student_dashboard),
            lambda: student_view_courses.view_registered_courses(user_email, student_dashboard),
            lambda: student_view_grades.view_marks_and_grades(user_email, student_dashboard),
            lambda: student_view_attendance.view_attendance(user_email, student_dashboard),
            lambda: student_apply_scholarship.apply_scholarship(user_email, student_dashboard),
            lambda: student_submit_assignment.submit_assignment(user_email, student_dashboard),
            lambda: student_download_material.download_materials(user_email, student_dashboard),
            lambda: student_give_feedback.give_feedback(user_email, student_dashboard),
            lambda: student_view_calendar.view_calendar(user_email, student_dashboard),
            lambda: student_drop_course.drop_courses(user_email, student_dashboard),
            lambda: student_communicateteachers.communicate_with_teacher(user_email, student_dashboard),
            lambda: student_apply_leaves.apply_leave(user_email, student_dashboard),
            lambda: student_view_transcript.display_transcript(user_email, student_dashboard),
            lambda: student_view_exam_schedule.view_material_table(user_email, student_dashboard)
        ]
    )
