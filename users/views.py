from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages # kind of like logging for django
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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

    if request.method == 'POST':
        # request.user == current user instance
        # to pass in POST data to Form, pass arg request.POST
        user_form = UserUpdateForm(request.POST,instance=request.user)
        # to pass files (image in this case), pass request.FILES argument
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            messages.success(request,f'Account updated!')

            # if no redirect, it will reload with POST request, instead of GET for profile
            return redirect('users-profile') # redirect to url named blog-home
    else :
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }
    
    return render(request, 'users/profile.html', context)