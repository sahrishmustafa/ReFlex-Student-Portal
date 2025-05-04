from pywebio.output import put_text, put_buttons, clear, put_markdown, put_success
from pywebio.input import input_group, input, textarea

from database.requests_db import insert_request

def submit_scholarship_application(data):
    student_id = data['student_id'];    request_type = "Scholarship Application";   reason = data['reason']
    insert_request(student_id, request_type, reason)
    print(f"Scholarship Application Submitted: {data}")  # Placeholder for DB storage

def apply_scholarship(email, return_dashboard):
    clear()
    put_markdown(f"### 🎓 Scholarship/Financial Aid Application - `{email}`")

    form_data = input_group("Application Form", [
        input("Full Name", name="name"),
        input("Student ID", name="student_id"),
        textarea("Reason for applying", name="reason")
    ])

    submit_scholarship_application(form_data)
    put_success("✅ Application submitted successfully!")
    put_buttons(['🔙 Back to Dashboard'], [lambda: return_dashboard(email)])
