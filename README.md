## Django To-Do Application
This is a Django-based To-Do List application that provides task management functionality for authenticated users. Each user has their own personal task list, and they can manage tasks (create, update, delete, mark as done) independently. Additionally, the application allows users to change their password, and reset it if forgotten, using a password reset email feature.

### Features
- User Authentication (Login, Logout, Registration)
- User-Specific Task Pages: Each logged-in user has their own dashboard where they can manage their personal tasks. No user can see another user's tasks.
- Task Management: Users can create, update, delete, and mark tasks as complete.
- Password Change: Users can change their password directly from their profile.
- Password Reset: In case a user forgets their password, they can reset it via an email link.
- Form rendering with crispy_forms and Bootstrap 4 integration

###Task Management
Users can:

- Create new tasks
- Update or edit tasks
- Delete tasks
- Mark tasks as done or complete

###Installation
Prerequisites
- Python 3.6+
- Django 4.2+
- Virtual Environment (recommended)

### Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```
### Install the required packages
```bash
pip install -r requirements.txt
```

#### Clone the repository:

```sh
git clone https://github.com/biossama/django-tasks-auth.git

````
