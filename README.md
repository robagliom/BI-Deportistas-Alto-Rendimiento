# BI-Deportistas-Alto-Rendimiento

1. Crear virtual env: python3 -m venv nombreEntorno (python3 -m venv proyectoFinal)
2. Activar entorno virtual: source proyectoFinal/bin/activate (windows: proyectoFinal\Scripts\activate.bat)
3. Instalar mysqlclient https://pypi.org/project/mysqlclient/
4. Instalar requerimientos: pip install -r requirements.txt
5. Crear archivo de configuración en bi_deportistas_alto_rendimiento/settings/local.py:
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
~~~