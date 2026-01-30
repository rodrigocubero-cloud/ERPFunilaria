from django.contrib import admin

from .models import Invoice, Payment


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "service_order", "issue_date", "due_date", "total", "status")
    list_filter = ("status", "issue_date")
    search_fields = ("service_order__id", "service_order__vehicle__plate")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("invoice", "paid_at", "amount", "method")
    list_filter = ("method", "paid_at")
    search_fields = ("invoice__id",)
