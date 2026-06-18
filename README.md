# Blog

A dynamic blog platform built with Python, HTML, and CSS.

## Overview

This repository contains a blog application that combines backend functionality with frontend presentation. The project demonstrates a well-balanced tech stack with a focus on Python for server-side logic and HTML/CSS for client-side rendering.

## Technology Stack

### Language Composition

- **Python** - 55% - Core backend logic and server-side processing
- **HTML** - 42.7% - Page structure and markup
- **CSS** - 2.3% - Styling and visual design

### Architecture

The project is structured around:
- **Backend**: Python-based application for handling business logic, data processing, and API endpoints
- **Frontend**: HTML templates for rendering blog pages and user interfaces
- **Styling**: CSS for responsive design and visual presentation

### Prerequisites

- Python 3.14
- A modern web browser
- (Additional dependencies may be listed in requirements.txt

  ## Installation & Local Setup
 Follow these steps to get the application running locally on your machine:
  
1. **Clone the repository and enter the project directory:**
   git clone [https://github.com/Mahesh-78-de/Blog.git](https://github.com/Mahesh-78-de/Blog.git)
   cd Blog

2. **Create and activate a isolated virtual environment:**
  # On Windows:
    python -m venv venv
    venv\Scripts\activate

   # On macOS/Linux:
     python3 -m venv venv
     source venv/bin/activate

3. **Install dependencies, initialize the database, and start the development server:**
   # Install required packages
       pip install -r requirements.txt

   # Generate database schema using Django migrations
       python manage.py migrate

   # Boot up the local development engine
       python manage.py runserver

4. Open your browser and navigate to the local server address (typically `http://localhost:5000` or similar)

## Project Structure


Blog/
├── .gitignore               # Excludes environment configurations and local databases
├── manage.py                # Django administrative command-line utility
│
├── blog_main/               # Project Configuration Directory
│   ├── static/              # Global static files
│   │   └── style.css        # Main stylesheet for the blog platform
│   ├── __init__.py
│   ├── asgi.py
│   ├── forms.py             # Global form handling configurations
│   ├── settings.py          # Central database settings and asset directory mappings
│   ├── urls.py              # Root-level URL routing patterns
│   └── views.py             # Custom global HTTP handlers
│
├── blog/                    # Core Blog Management Application
│   ├── migrations/          # Schema version control tracking
│   ├── __init__.py
│   ├── admin.py             # Content model exposure rules
│   ├── apps.py
│   ├── context_processor.py # Global context utilities (e.g., searchbar distribution)
│   ├── models.py            # Definitions for Posts, Categories, and Comments
│   ├── tests.py
│   ├── urls.py              # Application routing maps
│   └── views.py             # Business logic for home page feeds and details
│
├── dashboard/               # Core Administrator Operations Application
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── form.py              # Definitions for Post Creation and Modification forms
│   ├── models.py            # User management tracking tables
│   ├── tests.py
│   ├── urls.py              # Application routing maps for admin paths
│   └── views.py             # Logic for CRUD processes (Create, Update, Delete)
│
├── pages/                   # Static Information Management Application
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py             # Independent fallback routing engine
│
└── templates/               # Global Interface Markup Templates
    ├── 404.html             # Custom Resource Not Found template
    ├── base.html            # Core structural framing layout
    ├── blog.html            # Public blog platform listing page
    ├── category_posts.html  # Dynamic category filtering view
    │
    └── dashboard/           # Administrator Application Visual Templates
        ├── add_category.html
        ├── add_posts.html
        ├── add_users.html
        ├── categories.html
        ├── dashboard.html   # Central administrator dashboard template
        ├── edit_category.html
        ├── edit_posts.html
        ├── edit_users.html
        ├── posts.html       # Article listing management sheet
        ├── sidebar.html     # Navigation drawer layout fragment
        └── users.html       # Account listing table panel

## Usage & Features

### 🌐 Public Blog Interface
* **Smart Browsing & Search**: Filter posts via categories or find articles instantly using the persistent search bar.
* **Featured Feed**: Prominently highlights top-tier articles on the main homepage.

### 🔐 Administrative Dashboard (`dashboard.html`)
Access full CRUD operations via a secure content management control panel:
* **Posts (`posts.html`)**: Add, edit, or delete articles and manage publication statuses seamlessly.
* **Categories (`categories.html`)**: Expand platform topics dynamically with direct taxonomy management.
* **Users (`users.html`)**: Provision new user profiles and monitor system access controls.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

Please check the LICENSE file for licensing information.

## Author

**Mahesh-78-de**

---

**Last Updated**: June 2026
