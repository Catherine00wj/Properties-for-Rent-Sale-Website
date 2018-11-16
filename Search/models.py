from django.db import models

# Create your models here.
class Search(models.Model):
    city = models.CharField(max_length=64, default="")
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    parking = models.IntegerField()
    expectmoney = models.DecimalField(max_digits=12, decimal_places=2)

