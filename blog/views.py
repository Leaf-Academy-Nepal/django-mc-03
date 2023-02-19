from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog


class BlogListView(ListView):
    model = Blog
    queryset = Blog.objects.all()
    # select * from blog;
    template_name = "blog_list.html"

    #default key for blog_list is object_list

