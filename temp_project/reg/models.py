from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Statistics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ratio = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(10)
        ]
    )
    date = models.DateTimeField(auto_now=True)
