#coding=utf-8
from django.shortcuts import render
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from account.models import User
# Create your views here.
class UserForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=100)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())
    email=forms.EmailField(label='电子邮箱')
def register(request):
    if request.method=='POST':
        uf=UserForm(request.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            emali=uf.cleaned_data['email']
            user=User()#User models
            user.username=username
            user.password=password
            user.email=emali
            user.save()
            return render(request,'success.html',{'username':username})
    else:
        uf=UserForm()
        return render(request,'register.html',{'uf':uf})