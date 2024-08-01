from django.contrib import admin

from main.models import AdditionalCarImage, Car, Brand, Manufacturer

# Register your models here.
admin.site.register(AdditionalCarImage)
admin.site.register(Car)
admin.site.register(Brand)
admin.site.register(Manufacturer)