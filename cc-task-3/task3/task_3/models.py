from django.db import models

# Create your models here.

class task(models.Model):
    file_name = models.CharField(max_length=50)
    content = models.BinaryField()