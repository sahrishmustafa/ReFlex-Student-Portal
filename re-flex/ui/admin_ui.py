from pywebio.output import put_text, put_table, put_buttons, put_markdown, clear
from pywebio.input import input, file_upload

def admin_dashboard(user_email):
    from ui.admin_manage_timetables     import manage_timetables
    from ui.admin_update_exam_schedule  import update_exam_schedule
    from ui.admin_publish_course_offerings import publish_course_offerings
    from ui.admin_make_announcements    import make_announcements
    from ui.admin_handle_requests       import handle_requests

    clear()
    put_markdown('# 🛡️ Admin Dashboard')
    put_markdown(f"# 🎓 Welcome Admin, {user_email}!")
    put_buttons([
        'Manage Timetables', 'Update Exam Schedules', 'Publish Course Offerings',
        'Send Announcements', 'Handle Requests'
    ], onclick=[
        lambda: manage_timetables(admin_dashboard),
        lambda: update_exam_schedule(admin_dashboard),
        lambda: publish_course_offerings(admin_dashboard),
        lambda: make_announcements(admin_dashboard),
        lambda: handle_requests(admin_dashboard)
    ])
