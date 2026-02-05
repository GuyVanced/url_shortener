from django.urls import path
from . import views

app_name = "shortener"

urlpatterns = [
    path("", views.dashboard, name="home"),
    path("dashboard/", views.dashboard, name= "dashboard"),
    path("create/", views.create_short_url, name= "create_short_url"),
    path("delete/<int:pk>", views.delete_short_url, name="delete_short_url"),
    path("urls/<int:pk>/edit/", views.edit_url, name="edit_url"),
    
    # QR Code related URLs
    path("qr/<int:pk>/generate/", views.generate_qr_code_view, name="generate_qr_code"),
    path("qr/<int:pk>/view/", views.view_qr_code, name="view_qr_code"),
    path("qr/<int:pk>/download/", views.download_qr_code, name="download_qr_code"),
    path("qr/<int:pk>/regenerate/", views.regenerate_qr_code_view, name="regenerate_qr_code"),
    
    path("<str:short_code>/", views.redirect_short_url, name = "redirect"),
]
