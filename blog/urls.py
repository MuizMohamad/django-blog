from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'), 
]

# we can access this route through localhost:8000/blog/[endpoints/routes]
# why /blog ? because we defined /blog in urls.py in main project (blog-project) directory

# also add trailing / after endpoint, or it wouldnt work? in browser it will automatically add / after we type 
# localhost:8000/blog/about so it become ~/blog/about/ which if no 'about/' routes then no match