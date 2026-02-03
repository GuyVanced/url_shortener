from django.urls import path
from . import views

app_name = "shortener"

urlpatterns = [
    path("", views.dashboard, name= "dashboard"),
    path("<str:short_code>", views.redirect_view, name = "redirect")
]
