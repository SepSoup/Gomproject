from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Object(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    details = models.CharField(max_length=256, blank=False, null=False)
    found = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True, related_name="publisher")