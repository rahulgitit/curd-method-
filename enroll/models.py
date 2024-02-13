from django.db import models

# Create your models here.
class databaseintodolist(models.Model):
    title=models.CharField(max_length=100)
    descriptions=models.TextField()
