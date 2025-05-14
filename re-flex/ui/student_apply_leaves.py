from pywebio.output import put_text, put_buttons, clear, put_markdown, put_success
from pywebio.input import input_group, input, textarea

from database.requests_db import insert_request

def submit_leave_application(data):
    student_id = data['student_id']
    request_type = "Leave Application"
    reason = data['reason']
    insert_request(student_id, request_type, reason)
    print(f"Leave Application Submitted: {data}")  # Placeholder for DB storage

def apply_leave(email, return_dashboard):
    clear()
    put_markdown(f"### 📝 Leave Application - `{email}`")

    form_data = input_group("Leave Application Form", [
        input("Full Name", name="name", 
              validate=lambda name: "Name cannot be empty" if not name.strip() else None),
        
        input("Student ID", name="student_id", 
              validate=lambda sid: "Student ID must be numeric" if not sid.strip() else None),
        
        textarea("Reason for leave", name="reason", 
                 validate=lambda reason: "Please provide a reason for leave" if not reason.strip() else None)
    ])

    submit_leave_application(form_data)
    put_success("✅ Leave application submitted successfully!")
    put_buttons(['🔙 Back to Dashboard'], [lambda: return_dashboard(email)])
