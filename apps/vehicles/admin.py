from django.contrib import admin

from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("plate", "brand", "model", "year", "customer")
    search_fields = ("plate", "brand", "model", "customer__name")
    list_filter = ("brand", "year")
