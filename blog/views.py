from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

# so instead of typing the whole html as HttpResponse (string), we use template, 
# 
# steps: 
# 1. create a templates directory with a folder with same name as app (django convention)
# 2. add intended html file to the folder
# 3. add AppConfig (BlogConfig for this app) class to INSTALLED_APPS in main-project/settings.py
#    eg we add 'blog.apps.BlogConfig' string to the INSTALLED_APPS list 
#    (good practice to add this everytime we create app)
# 4. use render function imported from django.shortcuts

# also can add base template eg base.html for something that will appear in every html file (template inheritance)
# so for home we have base.html + home.html


def home(request):

    # how to pass data to html
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
