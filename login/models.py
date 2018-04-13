from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.



class Customer(models.Model):
    """docstring for Post"""
    name = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
