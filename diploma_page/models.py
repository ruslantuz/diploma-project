from django.db import models

# Create your models here.
class Offers(models.Model):
    location = models.CharField(max_length=100)
    rating = models.IntegerField()
    description = models.TextField(max_length=400)
    pricing = models.FloatField(max_length=10)
    offer_image = models.ImageField(null = True, blank=True, upload_to="images/")

    def __str__(self):
        return "id: " + str(self.id) + " - " + self.location
    
class Destinations(models.Model):
    place = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    dest_image = models.ImageField(null = True, blank=True, upload_to="images/")

    def __str__(self):
        return "id: " + str(self.id) + " - " + self.place