import sqlite3
import pandas as pd
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def view_material_table(user_email, back_function):
    """Display a material (ExamSchedule or Timetable) to students."""
    clear()
    put_markdown(f"### 📚 ExamSchedule for {user_email}")

    try:
        conn = sqlite3.connect('reflex.db')
        df = pd.read_sql_query(f"SELECT * FROM ExamSchedule", conn)
        conn.close()

        if df.empty:
            put_text(f"⚠️ No Exam Schedule found in the database.")
        else:
            put_table([df.columns.tolist()] + df.values.tolist())
    except Exception as e:
        put_text(f"❌ Failed to load Exam Schedule: {e}")

    put_buttons(['🔙 Back to Dashboard'], onclick=[lambda: back_function(user_email)])