from django.contrib import admin

from .models import Employee, ServiceOrder


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "active", "created_at")
    list_filter = ("active", "role")
    search_fields = ("name", "document")


@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "service_date",
        "plate",
        "vehicle_description",
        "customer",
        "employee",
        "status",
        "total_value",
    )
    list_filter = ("status", "service_date", "employee")
    search_fields = ("plate", "vehicle_description", "customer__name", "customer__document")
