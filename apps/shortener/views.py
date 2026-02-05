from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from .forms import ShortUrlForm, ShortUrlEditForm
from .services import generate_unique_short_code
from .models import ShortUrl
from .qr_service import generate_qr_code, regenerate_qr_code
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

@login_required
def dashboard(request):
    from django.db.models import Sum, Count, Q
    from django.utils import timezone
    
    urls = ShortUrl.objects.filter(user=request.user).order_by("-created_at")
    
    # Calculate analytics using database aggregation for better performance
    today = timezone.now().date()
    
    stats = urls.aggregate(
        total_clicks=Sum('click_count'),
        urls_with_qr=Count('id', filter=Q(qr_code_image__isnull=False)),
        created_today=Count('id', filter=Q(created_at__date=today))
    )
    
    context = {
        "urls": urls,
        "total_clicks": stats['total_clicks'] or 0,
        "created_today": stats['created_today'],
        "urls_with_qr": stats['urls_with_qr'],
    }
    
    return render(request, "shortener/dashboard.html", context)

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
            custom_code = form.cleaned_data["custom_short_code"]
            expires_at = form.cleaned_data["expires_at"]

            short_code = custom_code if custom_code else generate_unique_short_code()

            short_url = ShortUrl.objects.create(
                user = request.user,
                original_url = original_url,
                short_code = short_code,
                expires_at = expires_at

            )
            print(request.POST)
            print(form.cleaned_data)
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
        short_url = ShortUrl.objects.get(short_code= short_code, is_active=True)
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

@login_required
@login_required
def edit_url(request, pk):
    short_url = get_object_or_404(
        ShortUrl,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        form = ShortUrlEditForm(
            request.POST,
            instance=short_url
        )
        if form.is_valid():
            form.save()
            return redirect("shortener:dashboard")
    else:
        form = ShortUrlEditForm(instance=short_url)

    return render(
        request,
        "shortener/edit_url.html",
        {
            "form": form,
            "short_url": short_url
        }
    )


@login_required
def generate_qr_code_view(request, pk):
    """Generate QR code for a short URL"""
    short_url = get_object_or_404(
        ShortUrl,
        pk=pk,
        user=request.user
    )
    
    # Generate QR code
    success = generate_qr_code(short_url, request)
    
    if success:
        messages.success(request, "QR code generated successfully!")
        return redirect("shortener:view_qr_code", pk=pk)
    else:
        messages.error(request, "Failed to generate QR code. Please try again.")
        return redirect("shortener:dashboard")


@login_required
def view_qr_code(request, pk):
    """Display QR code for a short URL"""
    short_url = get_object_or_404(
        ShortUrl,
        pk=pk,
        user=request.user
    )
    
    if not short_url.has_qr_code:
        messages.warning(request, "QR code has not been generated yet.")
        return redirect("shortener:dashboard")
    
    return render(
        request,
        "shortener/qr_code_view.html",
        {"short_url": short_url}
    )


@login_required
def download_qr_code(request, pk):
    """Download QR code image"""
    short_url = get_object_or_404(
        ShortUrl,
        pk=pk,
        user=request.user
    )
    
    if not short_url.has_qr_code:
        messages.error(request, "QR code has not been generated yet.")
        return redirect("shortener:dashboard")
    
    try:
        response = HttpResponse(
            short_url.qr_code_image.read(),
            content_type='image/png'
        )
        response['Content-Disposition'] = f'attachment; filename="qr_code_{short_url.short_code}.png"'
        return response
    except Exception as e:
        messages.error(request, "Failed to download QR code.")
        return redirect("shortener:view_qr_code", pk=pk)


@login_required
def regenerate_qr_code_view(request, pk):
    """Regenerate QR code for a short URL"""
    short_url = get_object_or_404(
        ShortUrl,
        pk=pk,
        user=request.user
    )
    
    # Regenerate QR code
    success = regenerate_qr_code(short_url, request)
    
    if success:
        messages.success(request, "QR code regenerated successfully!")
        return redirect("shortener:view_qr_code", pk=pk)
    else:
        messages.error(request, "Failed to regenerate QR code. Please try again.")
        return redirect("shortener:dashboard")













