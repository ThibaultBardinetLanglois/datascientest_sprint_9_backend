from django.urls import path
from .views import health_check, trigger_error

urlpatterns = [
    path("", health_check, name="health_check"),
    path("triggered-error/", trigger_error, name="trigger_error")
]
