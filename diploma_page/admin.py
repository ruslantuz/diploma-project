from django.contrib import admin
from .models import  Destinations, Trips #, Offers, Planners
# Register your models here.

# admin.site.register(Offers)

admin.site.register(Destinations)

admin.site.register(Trips)
# admin.site.register(Planners)