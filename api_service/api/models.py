from django.db import models


class DataPoint(models.Model):
    name = models.CharField(max_length=30)
    t = models.IntegerField()
    v = models.DecimalField(max_digits=5, decimal_places=2)
