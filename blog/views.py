# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . models import Post


# Create your views here.
# def post(request):
#     return render(request, 'blog/post.html', {})
class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    
class BlogDetailView(DetailView):
    """docstring for BlogDetailView"""
    model =Post
    template_name = 'blog/post_detail.html'
    context_object_name='post_obj'