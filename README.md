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


## 🛠️ Installation & Setup

Follow these steps to get your development environment running locally:

### 1. Clone the Project
```bash
git clone [https://github.com/Sushil-Bhatta-sb/GAME_ZONE.git](https://github.com/Sushil-Bhatta-sb/GAME_ZONE.git)
cd GAME_ZONE