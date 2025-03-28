from django.core import validators as V
from django.db import models

from core.models import BaseModel


class UniversityModel(BaseModel):
    class Meta:
        db_table = 'universities'
        ordering = ['-id']

    name = models.CharField(max_length=100, unique=True, validators=[
        V.MinValueValidator(4, "University name must be 4 characters long")
    ])
