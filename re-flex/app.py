# app.py

from pywebio import start_server
from ui.student_ui import student_dashboard
from ui.faculty_ui import faculty_dashboard

def main():
    student_id = "S123"  # Later you can implement login and dynamically set this
    student_dashboard(student_id)
    fac_id="F001"
    faculty_dashboard(fac_id)

if __name__ == "__main__":
    start_server(main, port=8080)
