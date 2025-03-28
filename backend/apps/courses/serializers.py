from rest_framework import serializers

from .models import CourseModel


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = ('id', 'name')

    name = serializers.CharField(max_length=100, required=True)
