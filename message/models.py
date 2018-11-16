from django.db import models

# Create your models here.
# Message table
class Message(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    post_user = models.IntegerField()
    current_user = models.IntegerField()
    phone = models.IntegerField(default=123456)
    email_add = models.EmailField()
    messages = models.CharField(max_length=400)

    def __str__(self):
        return self.first_name


