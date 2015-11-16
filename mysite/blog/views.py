from django.shortcuts import render
from .models import *
# Create your views here.
def blog(request):
    blog_list=BlogPost.objects.all()
    return render(request,'blog.html',{'posts':blog_list})