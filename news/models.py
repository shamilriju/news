from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class news(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    image=models.ImageField(upload_to="pictures")
    place=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    reporter=models.CharField(max_length=100)
    date=models.DateTimeField(default=datetime.now,blank=True)
    description=models.TextField()

    def __str__(self):
        return '{}'.format(self.place)