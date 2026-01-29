from django.urls import path

from . import views

app_name = "services"

urlpatterns = [
    path("", views.dashboard, name="home"),
    path("painel/", views.dashboard, name="dashboard-legacy"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("ordens/nova/", views.create_service_order, name="service-order-create"),
    path("pedidos/nova/", views.create_service_order, name="service-order-legacy"),
]
