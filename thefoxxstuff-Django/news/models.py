from distutils.command import upload
from pyexpat import model
from turtle import title
from urllib import request
from django.db import models

from releases.views import album


class News(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Название')
    content = models.TextField(blank=True, verbose_name = 'Описание')
    data_created = models.DateField(auto_now_add=True, verbose_name = 'Дата')
    data_update = models.DateField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/', blank=True, verbose_name = 'Изображение')
    draft = models.BooleanField(default=True, verbose_name = 'На сайте')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-data_created']