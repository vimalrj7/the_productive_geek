from django.conf.urls import url
from django.views.generic import ListView, DetailView
from main.models import Post
from . import views
 
urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date"), template_name="main/home.html")),
    url(r'^about/', ListView.as_view(queryset=Post.objects.all(), template_name="main/about.html")),
    url(r'^books/', ListView.as_view(queryset=Post.objects.all(), template_name="main/books.html")),
    url(r'^(?P<slug>[-\w\d]+)/$', DetailView.as_view(model = Post, template_name = 'main/single.html')),
    ]  