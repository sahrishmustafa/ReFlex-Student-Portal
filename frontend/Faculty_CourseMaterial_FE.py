# faculty_panel.py

from pywebio import start_server
from pywebio.input import select, file_upload
from pywebio.output import put_text, put_buttons, put_table, clear

# Faculty-specific courses and sections (Assume fetched from login session)
faculty_courses = {
    "CS101": ["A", "B"],
    "CS102": ["B", "C"],
    "MATH101": ["A"],
    "MATH102": ["A", "C"]
}

uploaded_materials = {}

def upload_material(course, section):
    file = file_upload("Upload PDF", accept=[".pdf"])
    
    if course not in uploaded_materials:
        uploaded_materials[course] = {}
    uploaded_materials[course][section] = file
    
    clear()
    put_text(f"✅ Material for {course} (Section {section}) Uploaded Successfully!")
    put_buttons(["🔙 Back to Faculty Dashboard"], onclick=[faculty_dashboard])

def faculty_dashboard():
    clear()
    put_text("👨‍🏫 **Faculty Dashboard**")
    
    table_data = []
    for course, sections in faculty_courses.items():
        for section in sections:
            table_data.append([course, section, put_buttons(["Upload Material"], onclick=lambda btn, c=course, s=section: upload_material(c, s))])
    
    put_table([["Course", "Section", "Action"]] + table_data)
    put_buttons(["🔙 Back to Main Dashboard"], onclick=[lambda: None])

if __name__ == "__main__":
    start_server(faculty_dashboard, port=8082, debug=True)
