from pywebio.output import put_markdown, put_buttons, put_text, clear, put_file
from database.student_db import get_course_materials  # This should return a list of dicts with 'course', 'filename', 'content'

def download_materials(user_email, go_back_callback):
    clear()
    put_markdown(f"## 📥 Download Course Materials")

    materials = get_course_materials(user_email)

    if not materials:
        put_text("No materials available to download.")
    else:
        for item in materials:
            put_markdown(f"### 📘 {item['course']}: {item['filename']}")
            put_file(item['filename'], item['content'])

    put_buttons(['Back to Dashboard'], onclick=[lambda: go_back_callback(user_email)])
