from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(DeviceType)
admin.site.register(OperatingSystem)
# admin.site.register(VisitDate)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(City)


