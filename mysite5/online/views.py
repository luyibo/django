#coding=utf-8
from django.shortcuts import render,render_to_response
from django import forms
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
# Create your views here.
class UserForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=50)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())
def regist(request):
   if request.method=='POST':
       uf=UserForm(request.POST)
       if uf.is_valid():
           username=uf.cleaned_data['username']
           password=uf.cleaned_data['password']
           User.objects.create(username=username,password=password)
           return HttpResponse('register success!!')
   else:
       uf=UserForm()
   return render_to_response('regist.html',{'uf':uf},context_instance=RequestContext(request))

def login(request):
    if request.method=='POST':
       uf=UserForm(request.POST)
       if uf.is_valid():
           username=uf.cleaned_data['username']
           password=uf.cleaned_data['password']
           user=User.objects.filter(username=username,password=password)
           if user:
               response=HttpResponseRedirect('/index/')
               response.set_cookie('username',username,3600)
               return response
           else:
               return HttpResponseRedirect('/login/')
    else:
        uf=UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(request))

def index(request):
    username=request.COOKIES.get('username','')
    return render_to_response('index.html',{'username':username})

def logout(request):
    response=HttpResponse('logout')
    response.delete_cookie('username')
    return response