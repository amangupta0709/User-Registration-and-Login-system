# User-Registration-and-Login-system
a user registration and login logout system using Django and Postgresql Database

### Initialize the project

##### Create and activate a virtualenv:

1. `virtualenv venv`. This will a create a vitual environment called "venv" that helps with controlling dependencies.
2. `source venv/bin/activate`. 


##### Install dependencies:

(while in the activated virtual environment)
```bash
pip install -r requirements.txt
```
NOTE: After installing dependencies, pip-tools is also installed. You can now use it to manage package dependencies of your project.

Add a new package to requirements.in and run the following command to auto-update requirements.txt file
```bash
pip-compile requirements.in
```

Run the following command to sync your virtualenv
```bash
pip-sync`
```

##### Migrate, create a superuser, and run the server:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### PostgreSQL Setup
1. Download postgresql setup form https://www.postgresql.org/download/
2. Download pgadmin setup from https://www.pgadmin.org/download/
3. Start pgadmin and make a new database.

#### Security settings for Postgresql
There are a couple of security settings to setup manually. Open the DjangoProject/settings.py file and change USER and PASSWORD here: 
<pre>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database name',              #change this with your database name   
        'USER': 'postgres',                   #change this with your postgresql username. default is 'postgres'
        'PASSWORD': 'postgresql password',    #change this with your postgresql password
        'HOST': 'localhost',
    }
}
</pre>
