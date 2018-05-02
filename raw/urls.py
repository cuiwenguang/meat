from django.urls import path

from .views import collect_create

urlpatterns = [
    path('/collect/create', collect_create, name="collect_create"),
]