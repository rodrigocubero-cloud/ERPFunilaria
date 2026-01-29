from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "document", "email", "phone", "created_at")
    search_fields = ("name", "document", "email")
