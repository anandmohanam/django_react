

from django.db import models

class Person(models.Model):
    # Define model fields here
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    age = models.IntegerField()


def __str__(self):
        return self.name