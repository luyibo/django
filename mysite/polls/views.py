from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,authenticate,logout

from forms import *
# Create your views here.
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse('success')
        else:
            return HttpResponse( 'disabled account')

    else:
        return HttpResponse('invalid login')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username, email, password)
        if user is not None:
            user.save()
            return HttpResponse('ok')
        else:
            return HttpResponse('fail')
    else:return HttpResponse('aa')


def logo(request):
        if not request.user.is_authenticated():
            raise ('out')
        else:
            logout(request)
            return HttpResponse('OK')