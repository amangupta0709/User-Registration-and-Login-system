# User-Registration-and-Login-system
a user registration and login logout system using Django and Postgresql Database

### Initialize the project
Create and activate a virtualenv:

```bash
virtualenv venv
source venv/bin/activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```
NOTE: After installing dependencies, pip-tools is also installed. You can now use it to manage package dependencies of your project.
```bash
'''
Add a new package to requirements.in and run the following command to auto-update requirements.txt file
'''
pip-compile requirements.in

'''
Run the following command to sync your virtualenv
'''
pip-sync
```

Migrate, create a superuser, and run the server:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
