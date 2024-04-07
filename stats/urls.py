from django.urls import path

from .views import show_circuits

app_name = "stats"

urlpatterns = [path("circuits/", show_circuits, name="show_circuits")]
