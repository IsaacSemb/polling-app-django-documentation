from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.db.models import F
from django.views import generic

from polls.models import Choice, Question

# Create your views here.

class IndexView(generic.ListView):
    template_name="polls/index.html"
    context_object_name = "latest_questions_list"
    
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
    

# seeing details on a question 
def details(request, question_id):
    
    # get the question by id
    question = get_object_or_404( Question, pk=question_id )
    
    # context for the template
    context = {"question":question}
    
    return render( request, "polls/details.html", context )

# seeing results of a question
def results(request, question_id):
    
    # get question whoe results to show
    question = get_object_or_404(Question, pk=question_id)
    
    return render(request, 'polls/results.html', {"question":question})

# voting on a question
def vote(request, question_id):
    
    # get question to vote on
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get( pk = request.POST['choice'] )
        
    except (KeyError, Choice.DoesNotExist):
        # return form to the user to try again
        
        return render (
            request,
            'polls/details.html',
            {
                "question": question,
                "error_message": "You didnt select a choice"
            }
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        
        return HttpResponseRedirect( 
                                    reverse( 
                                            "polls:qtn_results", 
                                            args=(question.id,)
                                            )
                                    )
