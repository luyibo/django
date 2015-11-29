from django.db import models
from django.contrib import admin
# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=30)
    header=models.FileField(upload_to='./upload/')
    password=models.CharField(max_length=30)
    def __unicode__(self):
        return self.username

class Blog(models.Model):
    title=models.CharField(max_length=100)
    context=models.TextField()
    timestamp = models.DateTimeField()

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')


class comments(models.Model):
    tetx=models.TextField()