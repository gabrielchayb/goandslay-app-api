from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index, register , user_login , home , sair , visualizarperfil, editarperfil , deletarperfil , cadastrarlicao , listar_todas_licoes, editar_licao , deletar_licao

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
    path('licoes/', listar_todas_licoes, name='listar_todas_licoes'), # Rota para listar todas as lições de todos os usuarios
    path('licao/<int:licao_id>/editar/', editar_licao, name='editar_licao'), # Rota para editar uma lição SUA
    path('licao/<int:licao_id>/deletar/', deletar_licao, name='deletar_licao'), # Rota para deletar uma lição SUA
    path('api/licao/', include('licao.urls')),  # Incluindo URLs do app 'licao'
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),  # API Schema documentation
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),  # Swagger Docs
    path('api/user/', include('user.urls')),  # Incluindo URLs do app 'user'
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )