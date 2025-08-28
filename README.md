# nova_school_admin_py
Projecto practica de Python

# Crear entorno virtual para Python
python -m venv venv
# Linux
source venv/bin/activate
# Windows
.\venv\Scripts\Activate

# Instalar Python Django
pip install django
django-admin --version

pip install psycopg
# Windows
pip install "psycopg[binary]"

# Correr Django
python manage.py migrate
python manage.py runserver

# Pagina de la practica:
http://127.0.0.1:8000/subjects/