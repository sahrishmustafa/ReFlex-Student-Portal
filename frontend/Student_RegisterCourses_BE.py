from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to talk to backend

# SQLite Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student_portal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Student Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.Integer, nullable=False)

# Course Model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    semester_offered = db.Column(db.Integer, nullable=False)
    sections = db.Column(db.String(100), nullable=False)  # Example: "A,B,C"

# Enrollment Model
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    section = db.Column(db.String(10), nullable=False)

with app.app_context():
    db.create_all()

    # Check if test data already exists
    if Course.query.count() == 0:
        test_courses = [
            Course(name="Data Structures", semester_offered="2", sections="A,B,C"),
            Course(name="Operating Systems", semester_offered="3", sections="A,B"),
            Course(name="Database Systems", semester_offered="3", sections="A,C"),
            Course(name="Machine Learning", semester_offered="4", sections="A,B,C,D"),
        ]
        db.session.add_all(test_courses)
        db.session.commit()

# Route: Get Courses by Semester
@app.route('/get_courses', methods=['POST'])
def get_courses():
    data = request.json
    semester = data.get('semester')

    courses = Course.query.filter_by(semester_offered=semester).all()
    course_list = [{"id": c.id, "name": c.name, "sections": c.sections.split(",")} for c in courses]

    return jsonify(course_list)

# Route: Register Course
@app.route('/register_course', methods=['POST'])
def register_course():
    data = request.json
    student_id = data.get('student_id')
    course_id = data.get('course_id')
    section = data.get('section')

    enrollment = Enrollment(student_id=student_id, course_id=course_id, section=section)
    db.session.add(enrollment)
    db.session.commit()

    return jsonify({"message": "Course registered successfully!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=True)
