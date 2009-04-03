# coding=utf-8
from django.db import models

# 用户
class User(models.Model):
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    true_name = models.CharField(max_length=10)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField()