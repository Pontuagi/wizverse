from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, ProfileUpdateForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    '''register view implementation'''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = RegisterForm() 
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'registration/profile.html')


@login_required
def profileUpdate(request):
    if request.method == 'POST':
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if pform.is_valid():
            pform.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        pform = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'registration/profileUpdate.html', {'pform': pform})


@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)

    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'registration/profile_view.html', context)