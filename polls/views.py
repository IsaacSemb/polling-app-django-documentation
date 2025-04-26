from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from polls.models import Question

# Create your views here.
def index(request):
    
    # query latest 5 questions
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    # context data to pass to template
    context = {"latest_questions_list":latest_questions_list}
    
    # return HttpResponse("Hello, World. Youre at the polls index!")
    return render(request=request, template_name="polls/index.html", context=context)

# seeing details on a question 
def details(request, question_id):
    
    # get the question by id
    question = get_object_or_404( Question, pk=question_id )
    
    # context for the template
    context = {"question":question}
    
    return render( request, "polls/details.html", context )

# seeing results of a question
def results(request, question_id):
    response = f"Youre looking at question {question_id} results"
    return HttpResponse(response)

# voting on a question
def vote(request, question_id):
    return HttpResponse(f"Youre voting on question {question_id}")
