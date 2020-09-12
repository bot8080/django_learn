from django.db import models


# Create your models here.
class places(models.Model):
    name = models.CharField(max_length=101)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
