from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return HttpResponse("Hello Dashboard")

def redirect_view(request, short_code):
    return HttpResponse(f"Redirecting to users shortcode : {short_code}")

