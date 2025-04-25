from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World. Youre at the polls index!")

# seeing details on a question 
def details(request, question_id):
    return HttpResponse(f"Youre looking at question {question_id} details")

# seeing results of a question
def results(request, question_id):
    response = f"Youre looking at question {question_id} results"
    return HttpResponse(response)

# voting on a question
def vote(request, question_id):
    return HttpResponse(f"Youre voting on question {question_id}")
