from django.contrib import admin

from .models import Car


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'brand', 'year', 'color', 'plate', 'chassis_type', 'status', 'branch', 'image']