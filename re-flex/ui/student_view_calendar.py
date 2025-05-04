from pywebio.output import put_markdown, put_buttons, put_text, clear
from database.student_db import get_academic_calendar  # Dummy function returns text or calendar dates

def view_calendar(user_email, go_back_callback):
    clear()
    put_markdown("## 🗓️ Academic Calendar")

    calendar_info = get_academic_calendar()

    if calendar_info:
        put_text(calendar_info)
    else:
        put_text("Calendar not available at the moment.")

    put_buttons(['Back to Dashboard'], onclick=[lambda: go_back_callback(user_email)])
