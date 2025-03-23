from pywebio import start_server
from pywebio.output import put_buttons, put_text, clear, put_table
from pywebio.input import select

# Sample Data
courses = [
    ("Mathematics II", "MATH102"),
    ("Physics II", "PHYS102"),
    ("Data Structures", "CS102")
]

sections = ["A", "B", "C"]
registered_courses = {}

# Dashboard Navigation
def dashboard():
    clear()
    put_text("📌 **Student Dashboard**")
    put_buttons(
        ["📚 Register Courses", "📝 My Registered Courses", "⚙️ Settings"], 
        onclick=[show_courses, show_registered_courses, settings]
    )

# Course Registration
def register_course(course_code, section):
    registered_courses[course_code] = section
    clear()
    put_text(f"Successfully registered for {course_code} in section {section}")
    put_buttons(["🔙 Back to Dashboard"], onclick=[dashboard])

def select_section(course_code):
    section = select("Select Section", sections)
    register_course(course_code, section)

def show_courses():
    clear()
    put_text("📚 **Register for Courses**")
    
    table_data = []
    for name, code in courses:
        if code in registered_courses:
            table_data.append([name, code, "Registered"])
        else:
            table_data.append([name, code, put_buttons(["Register"], onclick=lambda btn, c=code: select_section(c))])
    
    put_table([["Course Name", "Course Code", "Action"]] + table_data)
    put_buttons(["🔙 Back to Dashboard"], onclick=[dashboard])

# Registered Courses Section
def show_registered_courses():
    clear()
    put_text("**My Registered Courses**")
    
    if not registered_courses:
        put_text("No courses registered yet.")
    else:
        put_table([["Course Code", "Section"]] + [[code, sec] for code, sec in registered_courses.items()])
    
    put_buttons([" Back to Dashboard"], onclick=[dashboard])

# Settings Section
def settings():
    clear()
    put_text("**Settings** (Coming Soon...)")
    put_buttons(["Back to Dashboard"], onclick=[dashboard])

# Run PyWebIO Server
if __name__ == "__main__":
    start_server(dashboard, port=8080, debug=True)
