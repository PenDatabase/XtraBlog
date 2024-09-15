from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post
from .forms import CreatePostForm, EditPostForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    context_object_name = "Posts"
    template_name = "posts/home.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"


class CreatePostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "posts/create_post.html"


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = "posts/edit_post.html"


class DeletePostView(DeleteView):
    model = Post
    template_name = "posts/delete_post.html"
    success_url = reverse_lazy("home")