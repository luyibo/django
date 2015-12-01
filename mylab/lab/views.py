from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forms import *
# Create your views here.
@login_required
def index(request):
    username=request.user.username
    article=Article(request.POST)

    return render_to_response('index.html',{'username':username})

