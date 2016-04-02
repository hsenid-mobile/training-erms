# ERMS
Enterprise Recruitment Managenent System

## Required Software

 - Python 2.7.5
 - Virtual env
 - Postgres 9.3

## Setup Environment

Install postgres and create a database called rms_db

Check/Modify the configuration in erms/erms/settings.py accordingly to connect your postgres

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rms_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
    }

Use the guide virtual-env-setup to setup a virtual environment
activate it and run below from project root folder to install dependent packages required to this project.

    'pip install -r requirements.txt' 

Check your Django version using this command within your activated virtual environment 
    
    python -c "import django; print(django.get_version())"

Go inside erms directory (Django project root) and run 
    
    python manage.py migrate
    
This will connect to your postgres rms_db and create cvm_candidate table 
with some other default auth, django related tables.

Create super user 

    python manage.py createsuperuser
    
Run applciation

    python manage.py runserver
    
This will start you app in http://127.0.0.1:8000/ check it in browser.
