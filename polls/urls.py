from django.urls import path
from . import views

# the name parameter is used to build the url using the url tag in templates
# the 'name' value as called by the {% url %} template tag

# adding namespace to an application 
# so that similar url patterns in app names can be distinguished
app_name = "polls"

urlpatterns = [
    path( "", views.IndexView.as_view(), name="index" ),
    path( "<int:pk>/details", views.DetailsView.as_view(), name="qtn_details" ),
    path( "<int:question_id>/results/", views.ResultsView.as_view(), name="qtn_results" ),
    path( "<int:question_id>/vote/", views.vote, name="qtn_vote" ),
    
] 
