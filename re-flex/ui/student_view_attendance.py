from pywebio.output import put_text, put_table, put_buttons, clear, put_markdown
from database.student_db import get_attendance_data
# Dummy data function for future DB

def view_attendance(email, return_dashboard):
    clear()
    put_markdown(f"### 📅 Attendance Record for: `{email}`")
    attendance_table = get_attendance_data(email)
    put_table(attendance_table)
    put_buttons(['🔙 Back to Dashboard'], [lambda: return_dashboard(email)])
