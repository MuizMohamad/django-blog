from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'), 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # pk means primary key
    path('post/create/', PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name = 'post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name = 'post-delete')
]

# class based view require to convert to class.as_view()

# we can access this route through localhost:8000/blog/[endpoints/routes]
# why /blog ? because we defined /blog in urls.py in main project (blog-project) directory

# also add trailing / after endpoint, or it wouldnt work? in browser it will automatically add / after we type 
# localhost:8000/blog/about so it become ~/blog/about/ which if no 'about/' routes then no match