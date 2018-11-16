from django.db import models
from datetime import datetime,date

# Create your models here.
class UserD(models.Model):  # Information on Users' login
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)
    legal = models.IntegerField(default=0)
    code=models.IntegerField(default=0)


class UserInfor(models.Model):
    Uid= models.ForeignKey(UserD,on_delete=models.CASCADE,to_field="id",unique=True)
    givenname = models.CharField(max_length=32,default="")
    familyname=models.CharField(max_length=32,default="")
    birthday=models.DateField(auto_created=True,default=datetime.strftime(date.today(), "%Y-%m-%d") )
    emailadd=models.EmailField(unique=True)
    job=models.CharField(max_length=255,default="")
    mobilenum=models.IntegerField(default=123456)
    manorwoman=(('male','man'),('female','woman'))
    gender=models.CharField(max_length=32,choices=manorwoman,default="male")


