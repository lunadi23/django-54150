from django.db import models

# Create your models here.
class Cliente(models.Model):
    apno = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    