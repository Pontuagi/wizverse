from django.shortcuts import render
from .models import tweet
from django.contrib.auth.decorators import login_required


# @login_required
def home(request):
    context = {'tweets': tweet.objects.all()}
    return render(request, 'home.html', context)

def landing(request):
    return render(request, 'landing.html')