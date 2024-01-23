# myapp/views.py
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Category
from django.shortcuts import render, redirect
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


# blog/views.py
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Change 'post_list' to your actual post list URL name
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})
