from django.db import models

# Create your models here.
class Outfits(models.Model):
    clothes_type=models.CharField(max_length=900)
    clothes_image=models.CharField(max_length=900)
    clothes_price=models.IntegerField()