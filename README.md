# ReFlex-Student-Portal

## Overview
Welcome to the **Student Portal** repository. This project aims to develop a web-based platform for university students to manage their academic activities efficiently. The portal will provide functionalities such as course registration, grade tracking, document submission, and communication with faculty members.

## Features
- User Authentication (Student, Faculty, Admin)
- Course Registration & Withdrawal
- Viewing Course List & Schedule
- Assignment Submission & Feedback
- Grade & Transcript Viewing
- Attendance Tracking
- Exam Scheduling & Results
- Fee Payment & History
- Student-Faculty Communication
- University Announcements & Notifications

## Project Structure (To Be Defined)
The repository will follow a structured approach:
- `/backend/` - Server-side code (APIs, Database, Business Logic)
- `/frontend/` - UI and UX implementation
- `/docs/` - Documentation and meeting notes
- `/tests/` - Automated tests and testing scripts

Note: The repository structure mentioned above may change in each sprint.

## Development Workflow
We are following an **Agile Scrum** methodology. The project will be divided into multiple sprints, with each sprint delivering a set of features.

## Architecture Overview
ReFlex follows a modular layered architecture:
- Presentation Layer: Built using PyWebIO for simplicity and speed
- Application Layer: Organized into role-specific files (student, faculty, admin)
- Data Layer: Uses SQLite3 for persistent storage and modular student_db.py for DB logic
- Routing Layer: Flask handles server startup and web routing
This architecture was chosen for its clarity, maintainability, and ease of development within a short academic timeline. PyWebIO enabled us to quickly prototype interactive features without needing deep frontend knowledge.

##  Technologies Used
Python 3.8
Flask – Routing and server logic
PyWebIO – Quick UI for web-based interactions without HTML/CSS/JS
SQLite3 – Lightweight embedded database


### Version Control
- Feature branches will be used for development.
- All code will be reviewed before merging into the main branch.
- Commit messages should be clear and descriptive.


---

## 🚀 How to Run

### Prerequisites

- Python 3.8 or above
- pip (Python package manager)

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/sahrishmustafa/ReFlex-Student-Portal.git
   cd ReFlex-Student-Portal/re-flex
   python app.py


## How to Contribute
1. Fork the repository.
2. Clone your forked repo.
3. Create a new feature branch.
4. Implement your changes and commit with descriptive messages.
5. Push to your fork and create a pull request.

