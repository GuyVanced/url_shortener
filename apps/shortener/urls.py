from django.urls import path
from . import views

app_name = "shortener"

urlpatterns = [
    path("dashboard/", views.dashboard, name= "dashboard"),
    path("create/", views.create_short_url, name= "create_short_url"),
    path("delete/<int:pk>", views.delete_short_url, name="delete_short_url"),
    path("urls/<int:pk>/edit/", views.edit_url, name="edit_url"),
    path("<str:short_code>/", views.redirect_short_url, name = "redirect"),
    
]
