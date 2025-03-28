from rest_framework import serializers

from .models import UniversityModel


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityModel
        fields = ('id', 'name')

    name = serializers.CharField(max_length=100, required=True)

    # def create(self, validated_data):
    #     return UniversityModel.objects.create(**validated_data)
