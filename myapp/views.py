from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Post

class Home(ListView):
    model = Post
    template_name = 'myapp/home.html'
    context_object_name = "Posts"
# Create your views here.


class About(TemplateView):

    template_name = 'myapp/about.html'
