from pywebio.output import put_markdown, put_buttons, put_text, clear, put_file

from database.material_db import get_course_materials  
from database.student_db import get_registered_courses_for_student

def download_materials(user_email, go_back_callback):
    clear()
    put_markdown(f"## 📥 Download Course Materials")

    registered_courses = get_registered_courses_for_student(user_email)
    print(registered_courses)
    materials = get_course_materials(registered_courses)

    if not materials:
        put_text("No materials available to download.")
    else:
        for item in materials:
            put_markdown(f"### 📘 {item['course']}: {item['filename']}")
            put_file(item['filename'], item['content'])

    put_buttons(['Back to Dashboard'], onclick=[lambda: go_back_callback(user_email)])
