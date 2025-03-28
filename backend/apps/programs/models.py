from django.core import validators as V
from django.db import models

from core.models import BaseModel


class ProgramModel(BaseModel):
    class Meta:
        db_table = 'programs'
        ordering = ['-id']

    name = models.CharField(max_length=100, unique=True, validators=[
        V.MinValueValidator(5, "Program name must be 5 characters long")
    ])
