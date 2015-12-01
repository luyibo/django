
from django.conf.urls import include, url
from django.contrib import admin
from auth_login import views

urlpatterns = [
    url(r'^register/$',views.register, name='register'),
    url('', include('django.contrib.auth.urls')),
]