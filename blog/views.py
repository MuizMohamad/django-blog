from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse

from .models import Post

from django.urls import reverse
from django.contrib import messages

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

# use django ListView
class PostListView(ListView):
    model = Post
    
    # by default, looking for template
    # <app>/<model>_<viewtype>.html
    # blog/Post_list.html
    
    # so need to change template
    # with template_name and change context name 
    # to the one we refer in template
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    
    # to change order of posts list
    # set ordering, with - to reverse from newest to oldest
    ordering = ['-date_posted']
    
    # list paging use this attribute
    paginate_by: int = 2
    

class PostDetailView(DetailView):
    model = Post

# expect post_form.html template
# context also expect form
# LoginRequiredMixin is like @login_required but for class based views
class PostCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Post
    
    # CreateView need to set field
    fields = ['title','content']
    
    # post will be created but error will occur because it not sure where to 
    # redirect after save
    # success-url also works but to pass self.pk we need to overwrite
    # get_####_url() function, #### == success or absolute
    # DEFINE GET_ABSOLUTE_URL ON THE MODEL
    
    # SuccessMessageMixin attribute
    success_message = 'Post successfully created'
    
    # author is current user logged in so need to overwrite 
    # form_valid method from CreateView superclass
    def form_valid(self,form):
        form.instance.author = self.request.user
        
        return super().form_valid(form)

# update is very similar to create
# UserPassesTestMixin to restrict non author user from updating post
# expect post_form template by default

class PostUpdateView(LoginRequiredMixin,SuccessMessageMixin,UserPassesTestMixin,UpdateView):
    
    model = Post
    
    # overwrite template so it show Update Post button instead of Create Post
    template_name = 'blog/post_form_update.html'
    
    # CreateView need to set field
    fields = ['title','content']
    
    # post will be created but error will occur because it not sure where to 
    # redirect after save
    # success-url also works but to pass self.pk we need to overwrite
    # get_####_url() function, #### == success or absolute
    # DEFINE GET_ABSOLUTE_URL ON THE MODEL
    
    # SuccessMessageMixin attribute
    success_message = 'Post successfully updated'
    
    # author is current user logged in so need to overwrite 
    # form_valid method from CreateView superclass
    def form_valid(self,form):
        form.instance.author = self.request.user
        
        return super().form_valid(form)

    # need to create function to work with UserPasseTestMixin
    def test_func(self):
        # return post object this view function is displaying
        post = self.get_object()
        
        if self.request.user == post.author :
            return True
        return False
    
# delete is similar to detail view
# UserPassesTestMixin to restrict non author user from updating post
# expect post_confirm_delete.html template by default
# context-name expect object by default
class PostDeleteView(LoginRequiredMixin,SuccessMessageMixin,UserPassesTestMixin,DeleteView):
    
    model = Post
    
    # success_url = 'blog-home'
    # SuccessMessageMixin attribute
    success_message = 'Post successfully deleted'
    
    def get_success_url(self):
        # SuccessMesssageMixin was used but this one also works
        # messages.success(self.request,"Post successfully deleted")
        return reverse('blog-home')
    
    # need to create function to work with UserPasseTestMixin
    def test_func(self):
        # return post object this view function is displaying
        post = self.get_object()
        
        if self.request.user == post.author :
            return True
        return False
    