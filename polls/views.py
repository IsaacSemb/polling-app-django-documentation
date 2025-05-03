from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone
from polls.models import Choice, Question


# Create your views here.

class IndexView(generic.ListView):
    template_name="polls/index.html"
    context_object_name = "latest_questions_list"
    
    def get_queryset(self):
        # return last five published question 
        # Ignore all questions in the future from now
        return Question.objects.filter( pub_date__lte=timezone.now() ).order_by("-pub_date")[:5]

class DetailsView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"
    
    # # intercept the query so that user cant get future questions
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
    

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    pk_url_kwarg = "question_id"
    

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
