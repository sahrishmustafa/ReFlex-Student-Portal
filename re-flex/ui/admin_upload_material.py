from pywebio.input import file_upload, select
from pywebio.output import put_markdown, put_text, clear, put_buttons

from database.adminmaterial_db import save_file_to_db

def manage_material(back_to_dashboard, user_email):
    """Allow admin to upload a material (Excel file) to the database."""
    clear()
    put_markdown(f"### 🗂 Upload Timetable (by {user_email})")

    # Upload the file
    material_type = select('Material', ['Timetable', 'ExamSchedule'])
    excel_file = file_upload("Upload Excel File", accept='.xlsx')

    if excel_file:
        file_content = excel_file['content']
        
        save_file_to_db(material_type, file_content)
        
        clear()
        put_text(f"✅ {material_type} uploaded by {user_email}")
        put_buttons(
            ['🔙 Back to Materials', '🏠 Back to Dashboard'],
            onclick=[back_to_dashboard, back_to_dashboard]
        )
