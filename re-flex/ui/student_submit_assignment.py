from pywebio.output import put_markdown, put_buttons, put_success, clear
from pywebio.input import file_upload, input

# Placeholder DB function
def save_assignment_upload(email, course, file):
    #####################################3
    #DB @ HERE
    #####################################3
    print(f"Assignment uploaded for {course} by {email}: {file['filename']}")

def submit_assignment(email, return_dashboard):
    clear()
    put_markdown(f"### 📝 Submit Assignment - `{email}`")

    course = input("Enter Course Name")
    file = file_upload("Upload your assignment file:", accept=".pdf .doc .docx .zip .c .cpp .py")

    save_assignment_upload(email, course, file)
    put_success(f"✅ {file['filename']} uploaded for {course}")

    put_buttons(['🔙 Back to Dashboard'], [lambda: return_dashboard(email)])
