# coding=utf-8
from django import forms
class Article(forms.Form):
     title = forms.CharField(
        label=u'文章标题',
        max_length=50,
        widget=forms.TextInput(),
        )

     content = forms.CharField(
        label=u'内容',
        min_length=10,
        widget=forms.Textarea(),
        #widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': u'事情是这样子的……'}),
        )
     author=forms.CharField(label=u'作者',
                            max_length=20,
                            )
     updated=forms.TimeField(label=u'时间')

