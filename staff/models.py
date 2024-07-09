from django.db import models
from django.contrib.auth.models import AbstractUser


class Staff(AbstractUser):
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Staff'

    def __str__(self):
        return self.username
