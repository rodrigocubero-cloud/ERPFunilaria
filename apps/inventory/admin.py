from django.contrib import admin

from .models import InventoryTransaction, Part


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ("sku", "name", "unit", "quantity", "price")
    search_fields = ("sku", "name")


@admin.register(InventoryTransaction)
class InventoryTransactionAdmin(admin.ModelAdmin):
    list_display = ("part", "transaction_type", "quantity", "service_order", "created_at")
    list_filter = ("transaction_type", "created_at")
    search_fields = ("part__sku", "part__name")
