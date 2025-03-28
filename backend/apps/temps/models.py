from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from core.models import BaseModel

from apps.courses.models import CourseModel
from apps.programs.models import ProgramModel
from apps.universities.models import UniversityModel

UserModel = get_user_model()


class TempModel(BaseModel):
    class Meta:
        db_table = 'temps'
        ordering = ['-id']

    semester = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(8)])
    is_public = models.BooleanField(default=False)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="temps")
    university = models.ForeignKey(UniversityModel, on_delete=models.CASCADE, related_name="temps")
    program = models.ForeignKey(ProgramModel, on_delete=models.CASCADE, related_name="temps")

    courses = models.ManyToManyField(CourseModel, through='TempCourseModel', related_name="temps")


class TempCourseModel(BaseModel):
    """
    Проміжна модель, що зв’язує TempModel та CourseModel
    """

    class Meta:
        db_table = 'temp_courses'
        unique_together = ('temp', 'course')

    temp = models.ForeignKey(TempModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.temp} - {self.course}"
