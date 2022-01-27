from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import haha,car,Ride,Relation

# Register your models here.


admin.site.register(Ride)
admin.site.register(haha)
admin.site.register(car)
admin.site.register(Relation)
