from rest_framework import serializers

from apps.courses.serializers import CourseSerializer

from .models import TaskModel


class TaskSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = TaskModel
        fields = ('id', 'name', 'type', 'status', 'deadline', 'course', 'course_id')

    def create(self, validated_data):
        course_id = validated_data.pop('course_id')
        return TaskModel.objects.create(course_id=course_id, **validated_data)

    def update(self, instance, validated_data):
        course_id = validated_data.pop('course_id', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if course_id is not None:
            instance.course_id = course_id

        instance.save()
        return instance
