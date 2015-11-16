from django.db import models
from django.contrib import admin
# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    time=models.DateTimeField()
    def __unicode__(self):
        return self.title
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','time')
