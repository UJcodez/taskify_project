from django.shortcuts import render, redirect
from .models import Card, UserProfile
from .forms import CardForm, SignUpForm, UserProfileForm, MyLoginForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home.html')

def card_list(request):
    if request.user.is_authenticated:
        cards = Card.objects.filter(user=request.user)
    else:
        cards = []  # An empty list when the user is not authenticated
    return render(request, 'card_list.html', {'cards': cards})

def delete_card(request, card_id):
    card = Card.objects.get(pk=card_id)
    card.delete()
    return redirect('card_list')

def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user  # Assign the current user
            card.save()
            return redirect('card_list')
    else:
        form = CardForm()
    return render(request, 'add_card.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()  # Save the User model to the database

            # Create or update the UserProfile associated with the user
            user_profile, _ = UserProfile.objects.get_or_create(user=user)
            user_profile.full_name = profile_form.cleaned_data['full_name']
            user_profile.save()

            return redirect('login')
    else:
        form = SignUpForm()
        profile_form = UserProfileForm()
    return render(request, 'signup.html', {'form': form, 'profile_form': profile_form})

class MyLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = MyLoginForm

def logoutUser(request):
    logout(request)
    return redirect('homepage')
