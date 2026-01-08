from django.shortcuts import render, get_object_or_404
from .models import Blog, Author, Tag
from .forms import CommentForm

# Create your views here.
def home(request):
    blogs=Blog.objects.all().order_by('-date')
    formdata=CommentForm()
    return render(request, 'blogs/index.html', {'blogs': blogs, 'formdata': formdata})

def post_detail(request, blog):
    blog_post = get_object_or_404(Blog, title=blog)
    return render(request, 'blogs/post.html', {'blog': blog_post})