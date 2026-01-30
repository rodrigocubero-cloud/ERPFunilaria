"""ASGI config for ERP Funilaria."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erpfunilaria.settings")

application = get_asgi_application()
