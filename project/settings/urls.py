"""bi_deportistas_alto_rendimiento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from modules.auxiliar import urls as auxiliar_urls
from modules.datoobjetivo import urls as datoobjetivo_urls
from modules.datosubjetivo import urls as datosubjetivo_urls
from modules.deportista import urls as deportista_urls
from modules.enfermedad import urls as enfermedad_urls
from modules.institucion import urls as institucion_urls
from modules.lesion import urls as lesion_urls
from modules.permiso import urls as permiso_urls
from modules.usuario import urls as usuario_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(auxiliar_urls)),
    path('datoobjetivo/', include(datoobjetivo_urls)),
    path('datosubjetivo/', include(datosubjetivo_urls)),
    path('deportista/', include(deportista_urls)),
    path('enfermedad/', include(enfermedad_urls)),
    path('institucion/', include(institucion_urls)),
    path('lesion/', include(lesion_urls)),
    path('permiso/', include(permiso_urls)),
    path('usuario/', include(usuario_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
