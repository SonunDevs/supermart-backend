from django.db import models

# Create your models here.
class Vendor(models.Model):
    shop_name = models.CharField(max_length=350)
    user_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='upload logo')
    user_email = models.EmailField(max_length=254)
    


