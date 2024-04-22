from django.contrib import admin
from .models import  Destinations, Orders, Reviews, Trips 
# Register your models here.

admin.site.register(Destinations)

admin.site.register(Trips)

admin.site.register(Orders)

admin.site.register(Reviews)
