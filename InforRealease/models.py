from django.db import models
from datetime import datetime,date

class ResourceInfor(models.Model):
    uid = models.IntegerField(default ="")
    city = models.CharField(max_length=64, default="")
    community = models.TextField()
    address = models.TextField()
    property = models.TextField()
    type = models.TextField()
    area = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    parking = models.IntegerField()
    expectmoney = models.DecimalField(max_digits=12, decimal_places=2)
    phone = models.IntegerField(default=123456)
    description = models.TextField(default="")
    # img = models.ImageField(upload_to='img',default="")
    img = models.TextField(default="")

    #img_url = models.FileField()
