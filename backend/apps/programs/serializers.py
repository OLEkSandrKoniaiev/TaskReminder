from rest_framework import serializers

from .models import ProgramModel


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramModel
        fields = ('id', 'name')

    name = serializers.CharField(max_length=100, required=True)
