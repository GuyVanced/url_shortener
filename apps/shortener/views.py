from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import ShortUrlForm
from .services import generate_unique_short_code
from .models import ShortUrl
from django.contrib.auth.decorators import login_required

def dashboard(request):
    return HttpResponse("Hello Dashboard")




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
        raise Http404("URL doesn't exist")
    
    short_url.click_count += 1
    short_url.save(update_fields=['click_count'])

    response = HttpResponseRedirect(short_url.original_url)
    return response




