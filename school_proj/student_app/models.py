from django.db import models
from django.core import validators as v

from .validators import validate_name_format, validate_email_format, validate_locker_combination

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null = False, blank = False, validators=[validate_name_format])
    student_email = models.EmailField(null = False, blank = False, unique=True, validators=[validate_email_format])
    personal_email = models.EmailField(null = False, blank = False, unique=True)
    locker_number = models.IntegerField(default = 110, null = False, blank = False, unique=True, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField( default="12-12-12",null = False, blank = False, max_length=10, validators=[validate_locker_combination])
    good_student = models.BooleanField(default=True)