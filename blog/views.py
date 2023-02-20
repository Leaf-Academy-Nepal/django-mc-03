from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog


class BlogListView(ListView):
    model = Blog
    queryset = Blog.objects.all()
    # select * from blog;
    template_name = "blog_list.html"

    #default key for blog_list is object_list


class BlogDetail(DetailView):
    model = Blog
    queryset = Blog.objects.all()
    template_name = "blog_detail.html"

    #default key - object

