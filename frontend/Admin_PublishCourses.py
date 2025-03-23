# admin_panel.py

from pywebio import start_server
from pywebio.input import select, checkbox
from pywebio.output import put_table, put_buttons, put_text, clear

# Sample course data categorized by semester
courses = {
    1: ["MATH101", "PHYS101", "CS101"],
    2: ["MATH102", "PHYS102", "CS102"],
    3: ["CS201", "CS202", "CS203"]
}

published_courses = {}

def publish_courses():
    clear()
    put_text("📢 **Publish Courses**")
    
    semester = select("Select Semester", list(courses.keys()), onchange=update_course_selection)
    update_course_selection(semester)

def update_course_selection(semester):
    clear()
    put_text("📢 **Publish Courses**")
    
    selected_courses = checkbox("Select Courses to Publish", options=courses[semester])
    
    published_courses[semester] = selected_courses
    put_buttons(["✅ Confirm Publish", "🔙 Back to Admin Dashboard"], 
                onclick=[lambda: confirm_publish(semester, selected_courses), admin_dashboard])

def confirm_publish(semester, selected_courses):
    published_courses[semester] = selected_courses
    clear()
    put_text(f"✅ Courses for Semester {semester} Published Successfully!")
    put_buttons(["🔙 Back to Admin Dashboard"], onclick=[admin_dashboard])

def get_published_courses():
    return published_courses

def admin_dashboard():
    clear()
    put_text("🛠️ **Admin Dashboard**")
    put_buttons(["📢 Publish Courses", "🔙 Back to Main Dashboard"], onclick=[publish_courses, lambda: None])

if __name__ == "__main__":
    start_server(admin_dashboard, port=8081, debug=True)
