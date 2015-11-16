#coding=utf-8
from django.db import models
from django.contrib import admin
# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('data publish')
    def __unicode__(self):
        return self.question_text
class Choice(models.Model):
    question=models.ForeignKey(Question)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text
class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=2
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('Date information',{'fields':['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date')
