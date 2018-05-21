from django.shortcuts import render, get_object_or_404

from .models import Blog
from jobs.models import Job

def allblogs(request):
    blogs = Blog.objects
    jobs = Job.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs, 'jobs':jobs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})
