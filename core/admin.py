from django.contrib import admin
from .models import Contact,Reservation,Item

# Register your models here.
admin.site.register(Contact)
admin.site.register(Reservation)
admin.site.register(Item)