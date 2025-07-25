from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Form(models.Model):
    code = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)