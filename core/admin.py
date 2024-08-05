from django.contrib import admin
from .models import Contact,Reservation,Subscribe,Team

# Register your models here.
admin.site.register(Contact)
admin.site.register(Reservation)

admin.site.register(Subscribe)
admin.site.register(Team)