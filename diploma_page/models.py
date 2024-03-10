from django.db import models
from django.contrib.auth.models import User
    
class Destinations(models.Model):
    place = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    dest_image = models.ImageField(null = True, blank=True, upload_to="images/")

    def __str__(self):
        return "id: " + str(self.id) + " - " + self.place
        
class Trips(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    cost = models.FloatField(max_length=10)
    days = models.IntegerField()
    rating = models.IntegerField()
    description = models.TextField(max_length=400)
    trip_image = models.ImageField(null = True, blank=True, upload_to="images/")
    is_special = models.BooleanField()
    
    def __str__(self):
        return "id: " + str(self.id) + " - " + self.title
    
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)

    person_count = models.IntegerField()
    check_in = models.DateField(blank=True, null=True)  
    check_out = models.DateField(blank=True, null=True)
    
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    placed_at = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending')
    
    def __str__(self):
        return f"Order {self.id} - User: {self.user.username} - Trip: {self.trip.title}"