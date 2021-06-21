from django.db import models
from django.contrib.auth.models import User
class AddTask(models.Model):
    Task = models.CharField(max_length=100)
    username = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE, null=True, blank=True)
    Date = models.DateField(blank=True, null=True)
    Time = models.TimeField(blank=True, null=True)