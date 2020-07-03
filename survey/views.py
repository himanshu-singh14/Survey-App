from django.shortcuts import render
from survey.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def surveyList(request):
    questions = Question.objects.all()
    context = { 'title':'survey', 'questions':questions }
    return render(request, 'survey/index.html', context)


@login_required(login_url="user-login")
def survey(request, id=None):
    if request.method == 'GET':
        user_id = request.user.id 
        question = Question.objects.get(id=id)
        context = { 'question':question }
        if Answer.objects.filter(user_id=user_id):
            context['already_exist'] = True
            context['answer'] = Answer.objects.get(user_id=user_id)
        else:
            context['already_exist'] = False
        return render(request, 'survey/survey.html', context)

    if request.method == 'POST':
        user_id = request.user.id        # It is used to get the login user
        data = request.POST['choice']
        if Answer.objects.filter(user_id=user_id):
            answer = Answer.objects.get(user_id=user_id)
            answer.delete()
        ret = Answer.objects.create(user_id=user_id, choice_id=data)
        if ret:
            return HttpResponseRedirect(reverse('survey-list'))
        else:
            return HttpResponse("Not Created")

