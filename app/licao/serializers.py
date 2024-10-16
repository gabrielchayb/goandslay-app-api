"""
Serializers for licao APIs
"""
from rest_framework import serializers

from core.models import Licao


class LicaoSerializer(serializers.ModelSerializer):
    """Serializer for Lessons."""

    class Meta:
        model = Licao
        fields = ['id', 'title', 'content', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']