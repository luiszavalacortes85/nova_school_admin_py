# nova_school_admin_py
Projecto practica de Python

# Crear entorno virtual para Python
python -m venv venv
source venv/bin/activate

# Instalar Python Django
pip install django
django-admin --version

pip install psycopg

# Correr Django
python manage.py migrate
python manage.py runserver

# Pagina de la practica:
http://127.0.0.1:8000/subjects/