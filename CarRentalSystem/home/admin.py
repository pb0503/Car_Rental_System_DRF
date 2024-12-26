from django.contrib import admin
from home.models import Customer, Car, Reservation

# Register your models here.
admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(Reservation)
