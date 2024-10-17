from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from core.models import Licao
from licao import serializers


class LicaoViewSet(viewsets.ModelViewSet):
    """View for manage Licao APIs."""
    serializer_class = serializers.LicaoSerializer
    queryset = Licao.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve licao for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        """Create a new Licao instance with the authenticated user."""
        serializer.save(user=self.request.user)