from rest_framework import serializers

from apps.courses.serializers import CourseSerializer

from .models import TempCourseModel, TempModel


class TempSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    course_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    )

    class Meta:
        model = TempModel
        fields = ('id', 'semester', 'is_public', 'user', 'university', 'program', 'courses', 'course_ids')
        read_only_fields = ('user',)

    def create(self, validated_data):
        course_ids = validated_data.pop('course_ids', [])
        validated_data['user'] = self.context['request'].user
        temp = TempModel.objects.create(**validated_data)

        TempCourseModel.objects.bulk_create([
            TempCourseModel(temp=temp, course_id=course_id) for course_id in course_ids
        ])

        return temp

    def update(self, instance, validated_data):
        course_ids = validated_data.pop('course_ids', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if course_ids is not None:
            instance.courses.clear()
            TempCourseModel.objects.bulk_create([
                TempCourseModel(temp=instance, course_id=course_id) for course_id in course_ids
            ])

        return instance
