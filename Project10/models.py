from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    fee = models.DecimalField(max_digits=20, decimal_places=3)