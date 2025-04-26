from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from polls.models import Question

# Create your views here.
def index(request):
    
    # query latest 5 questions
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    
    # create a string from all of them
    out_put = ", ".join([q.question_text for q in latest_questions_list])
    
    # get template you want to render
    template = loader.get_template("polls/index.html")
    
    # context data to pass to template
    context = {"latest_questions_list":latest_questions_list}
    
    # return HttpResponse("Hello, World. Youre at the polls index!")
    return HttpResponse(template.render(context=context, request=request))

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
