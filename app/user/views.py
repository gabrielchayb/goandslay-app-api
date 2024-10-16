"""
Views for the user API.
"""
from rest_framework import generics , authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View



from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
    LoginUserSerializer
)


class CreateUserView(View):
    """View para criar um novo usuário."""

    def get(self, request):
        form = UserSerializer()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        # Criar uma instância do serializer com os dados do request.POST
        serializer = UserSerializer(data=request.POST)
        
        # Validar os dados recebidos
        if serializer.is_valid():
            # Salvar os dados do novo usuário
            serializer.save()

            # Redirecionar o usuário autenticado para a página home
            return render(request, 'home.html', {'user': serializer.instance})

        # Se os dados não forem válidos, renderizar o formulário novamente com erros
        return render(request, 'register.html', {'form': serializer, 'errors': serializer.errors})


class LoginUserView(generics.GenericAPIView):
    """View for user login."""
    serializer_class = LoginUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """Handle user login."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data['user']
        
        # Log the user in
        login(request, user)

        # Redirecionar para a página home após o login
        return Response({'detail': 'Login successful', 'redirect_url': '/home/'})

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
    
    def delete(self, request, *args, **kwargs):
        """Delete the authenticated user."""
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)