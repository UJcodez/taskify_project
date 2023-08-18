from django import forms
from .models import Card, UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomPasswordInput(forms.PasswordInput):
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['autocomplete'] = 'new-password'  # To disable autocomplete
        context['widget']['attrs']['placeholder'] = self.attrs.get('placeholder', '')  # Optional placeholder
        context['widget']['attrs']['help_text'] = ''  # Set help_text to an empty string
        return context

class CardForm(forms.ModelForm):

    title = forms.CharField(
        label="",
        widget = forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-field'})
    )

    date = forms.DateField(
        label="",
        widget = forms.DateInput(attrs={'placeholder': 'Date (yyyy-mm-dd)', 'class': 'form-field'})
    )

    content = forms.CharField(
        label="",
        widget = forms.Textarea(attrs={'placeholder': 'Type something..', 'class': 'content-field'})
    )

    class Meta:
        model = Card
        fields = ['title', 'date', 'content']

class UserProfileForm(forms.ModelForm):
    full_name = forms.CharField(
        label="",
        widget = forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-field'})

    )

    class Meta:
        model = UserProfile
        fields = ('full_name',)  # Add other fields here if needed

class SignUpForm(UserCreationForm):

    username = forms.CharField(
        label="",
        widget = forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-field'})
        
    )

    password1 = forms.CharField(
        label="",
        strip=False,
        widget=CustomPasswordInput(render_value=True, attrs={'placeholder': 'Password', 'class': 'form-field'})
    )
    password2 = forms.CharField(
        label="",
        widget=CustomPasswordInput(render_value=True, attrs={'placeholder': 'Confirm Password', 'class': 'form-field'}),
        strip=False,
        help_text="",
    )

    profile_form = UserProfileForm()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class MyLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter username', 'class': 'form-login'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', 'class': 'form-login'}),
    )


