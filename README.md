# CRUD_APP# 🎮 GAME_ZONE - Full-Stack Django CRUD with Authentication

**GAME_ZONE** is a robust web application built with **Django 6.0**. It allows users to manage a collection of games while providing a secure environment through a built-in Authentication system. This project is a perfect example of modern Django development involving models, views, and template namespacing.

## 🚀 Key Features
* **User Authentication**: Complete Login, Logout, and Registration system.
* **Game Management (CRUD)**:
    * **Create**: Add new games with details.
    * **Read**: View a comprehensive list of all games.
    * **Update**: Edit information for existing games.
    * **Delete**: Remove game records from the database.
* **Access Control**: Secure views that ensure only authenticated users can modify data.
* **Responsive Design**: A clean, indented HTML structure ready for CSS styling.

---

## 📁 Project Structure
```text
GAME_ZONE/
├── crud_app/          # Project Root & Configuration
│   ├── settings.py    # Database, Apps, and Auth settings
│   └── urls.py        # Main routing (includes app URLs)
├── crud/              # Main Logic App
│   ├── migrations/    # Database history
│   ├── templates/     # Template Folder
│   │   └── crud/      # Namespaced sub-folder
│   │       ├── home.html      # Main Dashboard
│   │       ├── login.html     # Secure Login
│   │       └── register.html  # User Signup
│   ├── models.py      # Database Schema (Game Table)
│   ├── views.py       # Logic for CRUD & Auth
│   └── urls.py        # App-level routing
├── manage.py          # Django command-line utility
└── db.sqlite3         # SQLite Database


🛠️ Installation & Setup
Follow these steps to get your development environment running:

1. Clone the Project
Bash
git clone [https://github.com/Sushil-Bhatta-sb/GAME_ZONE.git](https://github.com/Sushil-Bhatta-sb/GAME_ZONE.git)
cd GAME_ZONE
2. Create and Activate Virtual Environment
Windows:

Bash
python -m venv venv
venv\Scripts\activate
Mac/Linux:

Bash
python3 -m venv venv
source venv/bin/activate
3. Install Django 6.0
Bash
pip install django
4. Database Setup (Migrations)
Apply the initial schema to your SQLite database:

Bash
python manage.py makemigrations
python manage.py migrate
5. Create a Superuser (Admin)
To access the Django Admin panel and manage users:

Bash
python manage.py createsuperuser
6. Run the Application
Bash
python manage.py runserver
Visit the app at: http://127.0.0.1:8000/crud/