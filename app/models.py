from django.db import models
from django.contrib.auth.models import User


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance = models.BooleanField(default=False)
    timeStamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username
        