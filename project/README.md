# BI-Deportistas-Alto-Rendimiento

1. Crear virtual env: python3 -m venv nombreEntorno (python3 -m venv proyectoFinal)
2. Activar entorno virtual: source proyectoFinal/bin/activate (windows: proyectoFinal\Scripts\activate.bat)
3. Instalar mysqlclient https://pypi.org/project/mysqlclient/
4. Instalar requerimientos: pip install -r requirements.txt
5. Crear archivo de configuración en settings/local.py:
~~~
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': nombre_db,  
        'USER': usuario,  
        'PASSWORD': contraseña,  
        'HOST': host,  
        'PORT': puerto
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your_account@gmail.com'
EMAIL_HOST_PASSWORD = 'your account’s password'
~~~
6. Crear migración BD: python manage.py migrate.