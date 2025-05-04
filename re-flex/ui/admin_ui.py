from pywebio.input import input, file_upload
from pywebio.output import put_text, put_table, put_buttons, put_markdown, clear

def admin_dashboard(user_email):
    from ui.admin_upload_material     import manage_material
    from ui.admin_publish_course_offerings import publish_course_offerings
    from ui.admin_make_announcements    import make_announcements
    from ui.admin_handle_requests       import handle_requests
    from database.admin_db              import get_admin_id_by_email

    admin_id = int(get_admin_id_by_email(user_email))

    clear()
    put_markdown('# 🛡️ Admin Dashboard')
    put_markdown(f"# 🎓 Welcome Admin, {user_email}!")
    put_buttons([
        'Upload Material', 'Publish Course Offerings',
        'Send Announcements', 'Handle Requests'
    ], onclick=[
        lambda: manage_material(admin_dashboard, admin_id),
        lambda: publish_course_offerings(admin_dashboard, admin_id),
        lambda: make_announcements(admin_dashboard, admin_id),
        lambda: handle_requests(admin_dashboard, admin_id)
    ])
