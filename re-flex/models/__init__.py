# database/init_db.py
import sqlite3

from models.admin import create_admin_table
from models.grade import create_grades_table
from models.section import create_section_table
from models.faculty import create_faculty_table
from models.student import create_student_table
from models.users import create_registered_users
from models.requests import create_request_table
from models.material import create_material_table
from models.studentquery import create_query_table
from models.attendance import create_attendance_table
from models.assignment import create_assignment_table
from models.course import create_course_table, create_faculty_course_table, create_student_course_table

def init_db():
    conn = sqlite3.connect('reflex.db')
    c = conn.cursor()

    # Call the functions to create tables
    create_registered_users(c)
    create_student_table(c)
    create_faculty_table(c)
    create_admin_table(c)
    create_course_table(c)
    create_section_table(c)
    create_grades_table(c)
    create_query_table(c)
    create_attendance_table(c)
    create_assignment_table(c)
    create_material_table(c)
    create_faculty_course_table(c)
    create_student_course_table(c)
    create_request_table(c)

    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Database initialized and populated.")
