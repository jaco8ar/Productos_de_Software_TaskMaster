from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	username = models.CharField(max_length=150, unique=True)
	password = models.CharField(max_length=128)
