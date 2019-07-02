from django.db import models


class Drug(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.PositiveIntegerField(default=0)

class Vitamin(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    drugs = models.ManyToManyField(Drug)

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    drugs = models.ManyToManyField(Drug)
