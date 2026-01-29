from datetime import timedelta

from django.db.models import Count, Sum
from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import DashboardFilterForm, ServiceOrderForm
from .models import ServiceOrder


def dashboard(request):
    today = timezone.localdate()
    default_start = today - timedelta(days=30)
    form = DashboardFilterForm(
        request.GET or None,
        initial={"start_date": default_start, "end_date": today},
    )

    if form.is_valid():
        start_date = form.cleaned_data["start_date"] or default_start
        end_date = form.cleaned_data["end_date"] or today
    else:
        start_date = default_start
        end_date = today

    orders = ServiceOrder.objects.filter(service_date__range=(start_date, end_date))
    total_revenue = orders.aggregate(total=Sum("total_value"))["total"] or 0

    nf_by_cnpj = (
        orders.exclude(nf_number="")
        .values("customer__document", "customer__name")
        .annotate(total_invoices=Count("id"), total_value=Sum("total_value"))
        .order_by("-total_value")
    )

    employee_rank = (
        orders.filter(employee__isnull=False)
        .values("employee__name")
        .annotate(total_orders=Count("id"), total_value=Sum("total_value"))
        .order_by("-total_value")
    )

    context = {
        "form": form,
        "start_date": start_date,
        "end_date": end_date,
        "total_revenue": total_revenue,
        "nf_by_cnpj": nf_by_cnpj,
        "employee_rank": employee_rank,
    }
    return render(request, "services/dashboard.html", context)


def create_service_order(request):
    if request.method == "POST":
        form = ServiceOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("services:service-order-create")
    else:
        form = ServiceOrderForm()

    return render(request, "services/service_order_form.html", {"form": form})
