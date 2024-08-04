from django.contrib import admin
from .models import Contact,Reservation,Item,Subscribe,Team

# Register your models here.
admin.site.register(Contact)
admin.site.register(Reservation)
admin.site.register(Item)
admin.site.register(Subscribe)
admin.site.register(Team)