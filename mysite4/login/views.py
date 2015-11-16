#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from .models import User
from django import forms
# Create your views here.
class UserForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=100)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())
def login(request):
    if request.method=='POST':
        uf=UserForm(request.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            user=User.objects.filter(username=username,password=password)
            if user:
                return render_to_response('success.html',{'username':username})
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf=UserForm()
    return render_to_response('login.html',{'uf':uf})