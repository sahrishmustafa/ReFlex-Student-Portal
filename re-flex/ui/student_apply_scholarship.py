from pywebio.output import put_text, put_buttons, clear, put_markdown, put_success
from pywebio.input import input_group, input, textarea

# Dummy logic to simulate application
def submit_scholarship_application(data):
    ########################################
    #DB @ HERE
    ########################################
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
