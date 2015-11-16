from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from disk.models import User
# Create your views here.
class Userform(forms.Form):
    username=forms.CharField()
    headImg=forms.FileField()

def register(request):
    if request.method=='POST':
        uf=Userform(request.POST,request.FILES)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            headImg=uf.cleaned_data['headImg']
            user=User()
            user.username=username
            user.headImg=headImg
            user.save()
    else:
        uf=Userform()
    return render(request,'register.html',{'uf':uf})
