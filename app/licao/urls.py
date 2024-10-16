"""
URL mappings for the licao app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from licao import views


router = DefaultRouter()
router.register('licao', views.LicaoViewSet)

app_name = 'Licao'

urlpatterns = [
    path('', include(router.urls)),
]