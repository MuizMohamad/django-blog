from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages # kind of like logging for django
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required # to restrict page to users
# Create your views here.

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save() # save the user to database
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}! You can log in now.')
        
            return redirect('login') # redirect to url named blog-home
        else :
            messages.error(request,f'Invalid registration info. Please fix the issues')
    else :
        form = UserRegisterForm()

    # to be passed to render html
    context = {
        'form' : form
    }

    return render(request,'users/register.html',context)


# to restrict page to user that are not logged in, add a decorator
@login_required
def profile(request):

    return render(request, 'users/profile.html')