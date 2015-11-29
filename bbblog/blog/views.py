from django.shortcuts import render
from django.contrib.auth import login,authenticate
# Create your views here.
def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        login(request, user)
        # Redirect to a success page.
        return HttpResponse("loggedin")
    else:
        # Show an error page
        return HttpResponse("invalid")
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponse("books")
    else:
        form = UserCreationForm()
    return render_to_response("register.html", {
        'form': form,
    })
from django.contrib import auth

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponse("loggedout")