from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.management import call_command
from .forms import ContactForm
from tours.models import Tour

# Create your views here.
# def home(request):
#     featured_tours = Tour.objects.filter(featured=True)
#     return render(request, 'pages/home.html', {'featured_tours': featured_tours})

def home(request):
    # get top 6 featured tours
    featured_tours = Tour.objects.all()[:6]

    contact_form = ContactForm()
    

    if request.method == "POST":
        if "contact_submit" in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.success(request, "Thank you! Your message has been received.")
                return redirect("home")

    # hero slides data
    hero_slides = [
        {
            'title': 'Discover Kenya',
            'description': 'Luxury safari & adventure tours',
            'image': 'images/hero.jpg',
            'button_text': 'Explore Tours',
        },
        {
            'title': 'Adventure Awaits',
            'description': 'Unforgettable travel experiences',
            'image': 'images/hero2.jpg',
        },
    ]

    context = {
        'featured_tours': featured_tours,
        'hero_slides': hero_slides,
        "contact_form": contact_form
    }

    # if request.method == "POST":
    #     name = request.POST.get("name")
    #     email = request.POST.get("email")
    #     message = request.POST.get("message")

    #     # later: save to DB or send email
    #     messages.success(request, "Thank you! We will contact you shortly.")
    
    return render(request, 'pages/home.html', context)

def setup_view(request):
    secret = request.GET.get('key')
    if secret != 'your-random-secret-string-here':
        return HttpResponse('Not authorized', status=403)
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@gmail.com', 'Frank@123')
        return HttpResponse('Superuser created successfully')
    return HttpResponse('Superuser already exists')