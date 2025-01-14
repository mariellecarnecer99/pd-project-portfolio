# Project Portfolio App

A project portfolio application built with Django and styled using Bootstrap. This app allows users to showcase their projects, and it also includes an admin panel for easy management of project entries.

## Features
- **Project Listing**: Displays a list of projects with relevant details.
- **Admin Panel**: Provides an admin interface for adding and managing projects.
- **Bootstrap Styling**: Clean and responsive design using Bootstrap.
- **Django Backend**: The app is powered by Django, offering a solid backend for handling data.
- **Search Functionality**: Allows users to search for projects by title.
- **Email Sending**: Enables sending emails, e.g., for project inquiries or notifications.

## Technologies Used
- **Django**: Web framework for the backend logic.
- **Bootstrap**: Frontend framework for styling and responsive design.
- **SQLite (or your choice of DB)**: Database for storing project details.

## Installation

### Prerequisites:
Make sure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Steps:

1. Clone this repository to your local machine:
   ```bash
   git clone <repository-url>
    ```

2. Navigate to the project directory:
    ```bash
    cd <project-directory>
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    ```

#### On Windows
venv\Scripts\activate
#### On macOS/Linux
source venv/bin/activate

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    
5. Run the migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser for accessing the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

8. Access the app in your browser at http://127.0.0.1:8000.

9. To access the admin panel, go to http://127.0.0.1:8000/admin and log in with the superuser credentials.

## Usage
In the admin panel, you can add, edit, and delete projects.
The main site will display the projects that are added through the admin panel.

## Contributing
Feel free to fork the repository and submit issues or pull requests for any improvements or bug fixes.