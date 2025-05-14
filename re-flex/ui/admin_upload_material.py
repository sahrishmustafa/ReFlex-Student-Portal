from pywebio.input import file_upload, select
from pywebio.output import put_markdown, put_text, clear, put_buttons

import io
import pandas as pd
from sqlalchemy import create_engine

def manage_material(back_to_dashboard, user_email):
    """Allow admin to upload a material (Excel file) to the database."""
    clear()
    put_markdown(f"### 🗂 Upload Material (by {user_email})")

    # Upload the file
    material_type = select('Material', ['Timetable', 'ExamSchedule'])
    excel_file = file_upload("Upload Excel File", accept='.xlsx')

    if excel_file:
        # Convert binary content to DataFrame using pandas
        file_content = excel_file['content']
        excel_buffer = io.BytesIO(file_content)
        
        try:
            df = pd.read_excel(excel_buffer)
        except Exception as e:
            put_text(f"❌ Error reading Excel file: {e}")
            return


        # Create SQLite engine
        engine = create_engine('sqlite:///C:/Users/Hadi/OneDrive/Documents/University/Software Engineering/Project/reflex.db')

        # Save DataFrame to SQL
        try:
            df.to_sql(material_type, engine, if_exists='replace', index=False)
        except Exception as e:
            put_text(f"❌ Error saving to database: {e}")
            return

        # Confirmation UI
        clear()
        put_text(f"✅ {material_type} uploaded and saved by {user_email}")

        put_buttons(['🔙 Back to Dashboard'], onclick=[lambda: back_to_dashboard(user_email)])

