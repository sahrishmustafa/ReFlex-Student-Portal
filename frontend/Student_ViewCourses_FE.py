# student_panel.py

from pywebio import start_server
from pywebio.output import put_table, put_buttons, put_text, clear
from pywebio.input import select
from Admin_PublishCourses import get_published_courses  # Import published courses from admin panel

# Sample course data categorized by semester
courses = {
    1: [("Mathematics I", "MATH101"), ("Physics I", "PHYS101"), ("Programming I", "CS101")],
    2: [("Mathematics II", "MATH102"), ("Physics II", "PHYS102"), ("Data Structures", "CS102")],
    3: [("Algorithms", "CS201"), ("Computer Networks", "CS202"), ("Operating Systems", "CS203")]
}

sections = ["A", "B", "C"]
registered_courses = {
    "MATH102": "A",
    "PHYS102": "B",
    "CS102": "C"
}

def dashboard():
    clear()
    put_text("📌 **Dashboard**")
    put_buttons(["👨‍🎓 Student Panel", "🛠️ Admin Panel"], onclick=[student_dashboard, lambda: None])

def student_dashboard():
    clear()
    put_text("📚 **Student Dashboard**")
    put_buttons([
        "📚 Register Courses", "📝 My Registered Courses", "🔙 Back"],
        onclick=[show_courses, show_registered_courses, dashboard]
    )

def register_course(course_code, section):
    registered_courses[course_code] = section
    clear()
    put_text(f"✅ Successfully registered for {course_code} in section {section}")
    show_courses()

def select_section(course_code):
    section = select("Select Section", sections)
    register_course(course_code, section)

def show_courses():
    clear()
    student_semester = 2  # Assume semester is determined dynamically
    published_courses = get_published_courses()
    
    if student_semester not in published_courses or not published_courses[student_semester]:
        put_text("No courses available for registration.")
        put_buttons(["🔙 Back to Student Dashboard"], onclick=[student_dashboard])
        return
    
    table_data = []
    for name, code in courses[student_semester]:
        if code not in published_courses[student_semester]:
            continue
        
        if code in registered_courses:
            table_data.append([name, code, "✅ Registered"])
        else:
            table_data.append([name, code, put_buttons(["Register"], onclick=lambda btn, c=code: select_section(c))])
    
    put_table([["Course Name", "Course Code", "Action"]] + table_data)
    put_buttons(["🔙 Back to Student Dashboard"], onclick=[student_dashboard])

def show_registered_courses():
    clear()
    put_text("📝 **My Registered Courses**")
    
    if not registered_courses:
        put_text("No courses registered yet.")
    else:
        table_data = [[name, code, section] for code, section in registered_courses.items() for name, c in sum(courses.values(), []) if c == code]
        put_table([["Course Name", "Course Code", "Section"]] + table_data)
    
    put_buttons(["🔙 Back to Student Dashboard"], onclick=[student_dashboard])

if __name__ == "__main__":
    start_server(dashboard, port=8080, debug=True)
