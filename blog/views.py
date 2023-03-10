from django.shortcuts import render, redirect, get_object_or_404
from blog.models import BlogPost
from django.db.models import Q
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm
from account.models import Account
from django.http import HttpResponse
import datetime


def create_blog_view(request):    
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must authenticate')
    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()
    context['form'] = form
    return render(request, 'blog/create_blog.html')

def detail_blog_view(request,slug):
    context = {}
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post
    try:
        check = BlogPost.objects.get(slug=slug)        
        check.visits = check.visits + 1
        check.save()
        return render(request, 'blog/detail_blog.html', context)
    except BlogPost.DoesNotExist:
        return render(request, 'blog/detail_blog.html', { 'error' :"error"})

def edit_blog_view(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must authenticate') 
    blog_post = get_object_or_404(BlogPost, slug=slug)
    if blog_post.author != user:
        return HttpResponse('You are not author of this post')
    if request.POST:
        form = UpdateBlogPostForm(
            request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = 'Updated'
            blog_post = obj
    form = UpdateBlogPostForm(
        initial={
            'title': blog_post.title,
            'body': blog_post.body,
            'image': blog_post.image,
            'pub_date': blog_post.pub_date

        }
    )
    context['form'] = form
    return render(request, 'blog/edit_blog.html', context)

def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        
        posts = BlogPost.objects.all().order_by('-date_published')[0:6]

        
        for post in posts:            
            queryset.append(post)
    return list(set(queryset))


