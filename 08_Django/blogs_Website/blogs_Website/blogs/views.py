from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog, Author, Tag, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    blogs=Blog.objects.all().order_by('-date')
    return render(request, 'blogs/index.html', {'blogs': blogs, })

@login_required
def post_detail(request, blog):
    blog_post = get_object_or_404(Blog, title=blog)
    comments=Comment.objects.filter(blog=blog_post).order_by('-id')
    if request.method=='POST':
        formdata=CommentForm(request.POST)
        if formdata.is_valid():
            new_comment=formdata.save(commit=False)
            new_comment.blog=blog_post
            new_comment.save()
            return redirect('post_detail',blog=blog_post.title)
    else:
        formdata=CommentForm()
    return render(request, 'blogs/post.html', {'blog': blog_post, 'formdata': formdata, 'comments': comments})