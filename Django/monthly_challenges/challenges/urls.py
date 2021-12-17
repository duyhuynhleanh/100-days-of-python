from django.urls import path
from . import views

urlpatterns = [
    path(route="<str:month>", view=views.monthly_challenge)
]
