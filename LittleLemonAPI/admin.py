from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.MenuItem)
admin.site.register(models.Category)
admin.site.register(models.Cart)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)