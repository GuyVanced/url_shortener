from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from .forms import ShortUrlForm, ShortUrlEditForm
from .services import generate_unique_short_code
from .models import ShortUrl
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

@login_required
def dashboard(request):
    urls = ShortUrl.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "shortener/dashboard.html", {"urls": urls})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect("shortener:dashboard")  # redirect to dashboard/homepage
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def create_short_url(request):
    if request.method == "POST":
        form = ShortUrlForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data["original_url"]

            short_code = generate_unique_short_code()

            short_url = ShortUrl.objects.create(
                user = request.user,
                original_url = original_url,
                short_code = short_code
            )
            return render(request,
                          "shortener/create_success.html",
                          {"short_url": short_url})
    else:
        form = ShortUrlForm()

    return render(request,
                  "shortener/create.html", {"form": form})

def redirect_short_url(request, short_code):
    """
    Increments the user's short_url click count by 1
    Redirects to the user's original url
    """
    try:
        short_url = ShortUrl.objects.get(short_code= short_code)
    except ShortUrl.DoesNotExist:
        return render(request,"404.html", status = 404)
    
    short_url.click_count += 1
    short_url.save(update_fields=['click_count'])

    response = HttpResponseRedirect(short_url.original_url)
    return response

@login_required
def delete_short_url(request, pk):
    try:
        short_url = ShortUrl.objects.get(pk = pk)
    except ShortUrl.DoesNotExist:
        return render(request,"404.html", status = 404)
    
    if short_url.user != request.user:
        return HttpResponseForbidden("You are not allowed here!")
    
    if request.method == "POST":
        short_url.delete()
        return redirect("shortener:dashboard")
    
    return render(
        request,"shortener/confirm_delete.html", {"short_url":short_url}
    )












