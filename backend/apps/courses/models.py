from django.core import validators as V
from django.db import models

from core.models import BaseModel


class CourseModel(BaseModel):
    class Meta:
        db_table = 'courses'
        ordering = ['-id']

    name = models.CharField(max_length=100, unique=True, validators=[
        V.MinValueValidator(2, "Course name must be 2 characters long")
    ])
