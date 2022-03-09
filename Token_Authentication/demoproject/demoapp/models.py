from django.db import models

# Create your models here.

class Student(models.Model):
    sname = models.CharField(max_length=32)
    scity = models.CharField(max_length=32)
    smarks = models.FloatField()

    def __str__(self):
        return '{}'.format(self.sname)
