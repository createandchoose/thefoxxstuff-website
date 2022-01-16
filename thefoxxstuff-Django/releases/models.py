from distutils.command import upload
from pyexpat import model
from turtle import title
from urllib import request
from django.db import models


class Album(models.Model):
    title = models.CharField(max_length = 150)
    content = models.TextField(blank=True)
    data_created = models.CharField(max_length = 150)
    cover = models.ImageField(upload_to='photos/%Y/%m/')
    draft = models.BooleanField(default=True)