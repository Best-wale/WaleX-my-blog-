
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post,Category

def post_list(request):
    posts = Post.objects.filter(published__lte=timezone.now()).order_by('-published')
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, slug):
	
    post = get_object_or_404(Post, slug=slug)
    category = Category.objects.all() 
    related_posts = Post.objects.filter(category=post.category).exclude(id=post.id).order_by('-published')[:5]
    return render(request, 'detail.html', {'post': post,'related_posts':related_posts,'category':category})


def posts_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category).order_by('-published')
    return render(request, 'personal.html', {'category': category, 'posts': posts})

def about_me(request):
	return render(request,'about.html',{})


def contact(request):
	return render(request,'contact.html',{})