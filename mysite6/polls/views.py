from django.shortcuts import render,render_to_response,get_object_or_404
from .models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.
def index(req):
    lastes_question_list=Question.objects.all()
    context={'lastes_question_list':lastes_question_list}
    return render_to_response('index.html',context)
def results(req,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render_to_response('results.html',{'question':question})
def detail(req,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render_to_response('detail.html',{'question':question})
def vote(req,question_id):
    p=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=p.choice_set.get(pk=req.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render_to_response('detail.html',{'question':p,'error-message':'You don not select a choice'})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results',args=(p.id,)))