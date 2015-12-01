from forms import RegisterForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render,render_to_response
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
             user=User.objects.create_user(username=form.cleaned_data.get('username'),
                                           password=form.cleaned_data.get('password'),
                                           email=form.cleaned_data.get('email'))
             return HttpResponse('success')
    else:form=RegisterForm()
    return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))
