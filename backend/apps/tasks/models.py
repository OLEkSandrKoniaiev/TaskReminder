from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from core.models import BaseModel

from apps.courses.models import CourseModel

UserModel = get_user_model()


class TaskModel(BaseModel):
    class Meta:
        db_table = 'tasks'
        ordering = ['-id']

    name = models.CharField(max_length=100, validators=[V.MinLengthValidator(2)])
    type = models.CharField(max_length=100, validators=[V.MinLengthValidator(2)])
    status = models.CharField(max_length=100, validators=[V.MinLengthValidator(2)])
    deadline = models.DateTimeField(null=True, blank=True)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="tasks")
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name="tasks")
