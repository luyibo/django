from django.db import models
from django.contrib import admin
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateTimeField()
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','date')
