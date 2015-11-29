#coding=utf-8
from django.shortcuts import render,render_to_response
from django import forms
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
class UserForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=50,help_text=u'昵称可用于登录，不能包含空格和@字符。',
        initial='',)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())
    #password2=forms.CharField(label='密码',widget=forms.PasswordInput())
    #email=forms.EmailField(label='mail',widget=forms.EmailInput())

def regist(request):
   if request.method=='POST':
       uf=UserForm(request.POST)
       if uf.is_valid():
           username=uf.cleaned_data['username']
           password=uf.cleaned_data['password']
           password2=uf.cleaned_data['password2']
           res = User.objects.filter(username=username)
           if len(res) != 0:
            raise forms.ValidationError(u'此昵称已经注册，请重新输入')
           if password==password2:
            User.objects.create(username=username,password=password)
            return HttpResponse('register success!!')
           else:raise forms.ValidationError('buyiyang')
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


def logout(request):
    response=HttpResponse('logout')
    response.delete_cookie('username')
    return response

class TextForm(forms.Form):
    title=forms.CharField(widget=forms.TextInput())
    content=forms.CharField(widget=forms.Textarea())

@login_required(login_url='login')
def index(request):
    username=request.COOKIES.get('username','')
    tf=TextForm()
    if tf.is_valid():
           title=tf.cleaned_data['title']
           text=tf.cleaned_data['text']
           Text.objects.create(title=title,text=text)
    return render_to_response('index.html',{'username':username,'tf':tf},context_instance=RequestContext(request))
