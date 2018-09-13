from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CandidateForm, CandidateRating
from .models import Technology, Questions, Result, Candidate
import json

@login_required
def home(request):
    if not request.user.is_superuser:
        return redirect('login')
    else:
        form = CandidateForm()
        if request.method == 'POST':
            form = CandidateForm(request.POST)
            if form.is_valid():
                user=form.save()
                return redirect('questions',user=user.id)
        else:
            form = CandidateForm()
        return render(request, 'home.html', {'form':form})

@login_required
def questions(request, user):
    #TODO need to apply pagination
    questions = Questions.objects.all()
    return render(request, 'questions.html', {'userid':user, 'questions':questions})

@login_required
def ratings(request):
    #SuperUser submit rating for perticular questions
    if request.is_ajax():
        rating_form = CandidateRating(request.POST)
        user = request.POST.get('userId')
        if rating_form.is_valid():
            rating_form.save()
            return HttpResponse('Success')
    return HttpResponse('wrong ratings')

@login_required
def result(request, user):
    result = Result.calculation(user)
    return redirect('home')

@login_required
def result_index(request):
    result = Result.objects.all()
    data=[]
    for i in result:
        percentage = json.loads(i.questions)
        data.append({'name':i.candidate.name, 'total_ratings':i.total_ratting, 'percentage':percentage})

    return render(request, 'result_index.html', {'data':data})