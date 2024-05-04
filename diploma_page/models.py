from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

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
    description = models.TextField(max_length=400)
    trip_image = models.ImageField(null = True, blank=True, upload_to="images/")
    is_special = models.BooleanField()
    
    @property
    def rating(self):
        list = Reviews.objects.filter(trip=self.id).all()
        try:
            rate = list.aggregate(Sum('rating'))['rating__sum']/len(list)
        except: 
            rate = 1
        return rate
    
    def __str__(self):
        return "id: " + str(self.id) + " - " + self.title
    
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)

    person_count = models.IntegerField()
    check_in = models.DateField(blank=True, null=True)  
    check_out = models.DateField(blank=True, null=True)
    
    placed_at = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending')
    
    @property
    def total_price(self):
        return self.person_count * self.trip.cost
    
    def __str__(self):
        return f"Order {self.id} - User: {self.user.username} - Trip: {self.trip.title}"
    
class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)

    text = models.TextField(max_length=1000)
    avatar = models.ImageField(upload_to="images/", default="images/default-avatar.png")
    rating = models.IntegerField()

class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=3000)
    image = models.ImageField(null = True, blank=True, upload_to="images/")

 

