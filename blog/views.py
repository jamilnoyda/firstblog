# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, DetailView ,UpdateView, DeleteView
from django.shortcuts import render,redirect
from . models import Post
from .forms import PostForm
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy, reverse






class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView):
    """docstring for BlogDetailView"""
    model =Post
    template_name = 'blog/post_detail.html'
    context_object_name='post_obj'

class PostUpdate(UpdateView):
    model = Post
    #success_url = reverse_lazy('blog:post_detail')
    success_url = reverse_lazy('blog:home')

    fields = ['title', 'author', 'text']
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('../'+str(post.pk)+'/detail/post_detail')

            
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})