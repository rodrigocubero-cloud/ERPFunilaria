from django import forms

from .models import ServiceOrder


class DashboardFilterForm(forms.Form):
    start_date = forms.DateField(
        label="Data inicial",
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    end_date = forms.DateField(
        label="Data final",
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
    )


class ServiceOrderForm(forms.ModelForm):
    class Meta:
        model = ServiceOrder
        fields = [
            "service_date",
            "plate",
            "vehicle_description",
            "total_value",
            "customer",
            "nf_number",
            "ss_number",
            "employee",
            "description",
            "status",
        ]
        widgets = {
            "service_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }
