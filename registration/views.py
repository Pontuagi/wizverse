from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.
def register(request):
    '''register view implementation'''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = RegisterForm() 
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    return render(request, 'registration/profile.html')