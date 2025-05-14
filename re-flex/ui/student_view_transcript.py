from pywebio.input import input
from pywebio.output import put_table, put_text, put_markdown, clear, put_buttons

from database.grade_db import fetch_transcript
from database.student_db import get_student_id_by_email

def display_transcript(email, return_dashboard):
    clear()
    put_markdown(f"## 📄 Academic Transcript - `{email}`")

    student_id = get_student_id_by_email(email)

    transcript = fetch_transcript(student_id)

    if not transcript:
        put_text("❌ No grades found for this Student ID.")
    else:
        for course, records in transcript.items():
            put_markdown(f"### 📘 {course}")
            table_data = [["Assessment Type", "Total Marks", "Obtained Marks"]]
            for record in records:
                table_data.append([record['type'], record['total'], record['obtained']])
            put_table(table_data)

    put_buttons(['🔙 Back to Dashboard'], [lambda: return_dashboard(email)])
