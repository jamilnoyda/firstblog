# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# class Post(models.Model):
#     """docstring for Post"""
#     author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
#     title = models.CharField(max_length = 200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
    
#     published_date = models.DateTimeField(blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title
class Post(models.Model):
    
    created_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    author  = models.CharField(max_length = 200)
    text = models.TextField()

    def __str__(self):
        return self.title
