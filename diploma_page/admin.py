from django.contrib import admin
from .models import  Destinations, Orders, Trips #, Offers, Planners
# Register your models here.

# admin.site.register(Offers)


admin.site.register(Destinations)

admin.site.register(Trips)

admin.site.register(Orders)
# admin.site.register(Planners)