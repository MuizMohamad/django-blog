
from re import L
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# to add another field to UserCreationForm (for login)
# we need to create new form that inherit from UserCreatioForm

# custom form
class UserRegisterForm(UserCreationForm):

    # so the form will have all base fields + email
    email = forms.EmailField()

    # configuration class
    # we want this form to interact with model User
    class Meta:
        # so when we do form.save() we want to save to 
        # User model
        model = User 
        fields = ['username','email','password1','password2']

# form for updating user info  
class UserUpdateForm(forms.ModelForm):
    
    # so the form will have all base fields + email
    email = forms.EmailField()

    # configuration class
    # we want this form to interact with model User
    class Meta:
        # so when we do form.save() we want to save to 
        # User model
        model = User 
        fields = ['username','email']

# form for updating user profile
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']