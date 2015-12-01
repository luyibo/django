from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django import forms
from models import User

from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
# Create your views here.
class UserForm(forms.Form):
    username=forms.CharField(label='name',max_length=30)
    password=forms.CharField(label='password',widget=forms.PasswordInput())

class BlogForm(forms.Form):
    pass


def register(req):
    if req.method=='POST':
        uf=UserForm(req.POST,req.FILES)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            filterr=User.objects.filter(username=username)
            if len(filterr)>0:
                return HttpResponse('existed')
            else:

                User.objects.create(username=username,password=password)
            return HttpResponse('register success')
    else:
        uf=UserForm()
    return render_to_response('register.html',{'uf':uf},context_instance=RequestContext(req))

def login(req):
    if req.method=='POST':
        uf=UserForm(req.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            user=User.objects.filter(username=username,password=password)
            if user:
                response=HttpResponseRedirect('/index/')
                response.set_cookie('username',username,3600)
                return response
            else:return HttpResponse('error')
    else:
        uf=UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

def index(req):
    username=req.COOKIES.get('username','')
    return render_to_response('index.html',{'username':username})

def logout(req):
    response=HttpResponseRedirect('/login/')
    response.delete_cookie('username')
    return response

class TextForm(forms.Form):
    title=forms.CharField()
    content=forms.TimeField()

