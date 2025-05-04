from pywebio import start_server
from pywebio.input  import input, select, TEXT, PASSWORD
from pywebio.output import put_markdown, clear

from ui.student_ui import student_dashboard
from ui.faculty_ui import faculty_dashboard
from ui.admin_ui   import admin_dashboard

def main():
    clear()
    put_markdown("# 🔐 ReFlex Login")
    email = input("Enter your email", type=TEXT, placeholder="you@example.com")
    # password = input("Password", type=PASSWORD)
    role  = select("I am logging in as a…", ["Student", "Faculty", "Admin"])

    if role == "Student":
        student_dashboard(email)
    elif role == "Faculty":
        faculty_dashboard(email)
    else:
        admin_dashboard(email)

if __name__ == "__main__":
    start_server(main, port=8080, debug=True)
