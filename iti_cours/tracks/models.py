from django.db import models

class Track(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    bo=models.BooleanField(default=True)
# Create your models here.
