"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index, register , user_login , home , sair , visualizarperfil, editarperfil , deletarperfil , cadastrarlicao , visualizarlicao, editarlicao , deletarlicao # Importando as views que você precisa

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para a interface de administração
    path('', index, name='index'),  # Página inicial
    path('register/', register, name='register'),  # Rota para o registro
    path('user_login/', user_login, name='user_login'),  # Rota para o login
    path('home/', home, name='home'),  # Rota para a home
    path('sair/', sair, name='sair'),  # Rota para o logout
    path('visualizarperfil/', visualizarperfil, name='visualizarperfil'),  # Rota para visualizar o perfil
    path('editarperfil/', editarperfil, name='editarperfil'),  # Rota para editar o perfil
    path('deletarperfil/', deletarperfil, name='deletarperfil'),  # Rota para deletar o perfil
    path('cadastrarlicao/', cadastrarlicao, name='cadastrarlicao'),  # Rota para cadastrar uma lição
    path('visualizarlicao/', visualizarlicao, name='visualizarlicao'),  # Rota para visualizar uma lição
    path('editarlicao/', editarlicao, name='editarlicao'),  # Rota para editar uma lição
    path('deletarlicao/', deletarlicao, name='deletarlicao'),  # Rota para deletar uma lição
    path('api/licao/', include('licao.urls')),  # Incluindo URLs do app 'licao'
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),  # API Schema
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),  # Swagger Docs
    path('api/user/', include('user.urls')),  # Incluindo URLs do app 'user'
]

# Serve arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )