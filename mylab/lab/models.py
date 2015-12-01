from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    content = models.TextField()
    updated = models.DateTimeField()
    def __unicode__(self):
        return self.title