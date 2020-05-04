from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Trip)
admin.site.register(models.Passenger)
admin.site.register(models.Stop)
admin.site.register(models.Assistant)

