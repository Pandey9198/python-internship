# Django Todo Project

A simple Django-based todo application with full CRUD functionality.

## Features

- Create, read, update, and delete todo items
- Mark todos as pending or completed
- Add descriptions and due dates to todos
- Django admin interface for management
- Responsive HTML templates

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone or navigate to the project directory:
```bash
cd todo_project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin account):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Open your browser and navigate to:
   - Application: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Project Structure

```
todo_project/
├── manage.py                 # Django management script
├── requirements.txt          # Project dependencies
├── db.sqlite3               # SQLite database (created after migrations)
├── todo_project/            # Project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
└── todo_app/                # Main application
    ├── migrations/          # Database migrations
    ├── static/              # Static files (CSS, JS)
    ├── templates/           # HTML templates
    ├── models.py            # Database models
    ├── views.py             # View functions
    ├── forms.py             # Django forms
    ├── urls.py              # App URL routing
    ├── admin.py             # Admin configuration
    └── tests.py             # Unit tests
```

## API Endpoints

- `GET /` - List all todos
- `GET /todo/<id>/` - View todo details
- `GET /create/` - Create todo form
- `POST /create/` - Create new todo
- `GET /todo/<id>/update/` - Edit todo form
- `POST /todo/<id>/update/` - Update todo
- `GET /todo/<id>/delete/` - Delete confirmation
- `POST /todo/<id>/delete/` - Delete todo
- `POST /todo/<id>/toggle/` - Toggle todo status

## Usage

### Creating a Todo
1. Click "Create Todo" button
2. Fill in the form with title, description (optional), status, and due date
3. Submit the form

### Updating a Todo
1. Click on a todo to view details
2. Click "Edit" button
3. Modify the fields
4. Submit the form

### Deleting a Todo
1. Click on a todo to view details
2. Click "Delete" button
3. Confirm deletion

### Toggling Todo Status
- Click the status button on the todo list to toggle between pending and completed

## Admin Interface

Access the Django admin panel at `/admin/` with your superuser credentials to:
- Manage todos
- Filter by status or creation date
- Search todos by title or description

## Running Tests

```bash
python manage.py test
```

## License

This project is open source and available under the MIT License.
