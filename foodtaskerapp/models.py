from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
        # 'user' defines who is the owner of the restaurant
        # 'OnetoOneField' means one user has a one  restaurant and one restaurant belongs to one restaurant
        # 'on_delete = models.CASCADE' means once you delete that user you also delete the restaurant associated to that user as well
    user  = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'restaurant')
    name = models.CharField(max_length = 500)
    phone = models.CharField(max_length = 500)
    address = models.CharField(max_length = 500)
    logo = models.ImageField(upload_to='restaurant_logo', blank=False)

    def __str__(self):
        return self.name  #used to display the ID of the restaurant object (self.name for name / self.address for adress)
