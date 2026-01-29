from django.urls import path

from . import views

app_name = "services"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("ordens/nova/", views.create_service_order, name="service-order-create"),
]
