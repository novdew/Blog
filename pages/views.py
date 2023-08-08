from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import PostForm


# Create your views here.
class CreatePage(generic.CreateView):
    model = Post
    template_name = 'pages/new.html'
    fields = ['title', 'body', 'image']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class HomePage(generic.ListView):
    model = Post
    template_name = 'pages/home.html'
    context_object_name = 'posts'


class DetailPage(generic.DetailView):
    model = Post
    template_name = 'pages/detail.html'
    context_object_name = 'post'


class EditPage(generic.UpdateView):
    model = Post
    template_name = 'pages/edit.html'
    form_class = PostForm
    success_url = reverse_lazy('home')


class DeletePage(generic.DeleteView):
    model = Post
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('home')
