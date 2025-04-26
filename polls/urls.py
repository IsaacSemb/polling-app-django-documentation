from django.urls import path
from . import views

# the name parameter is used to build the url using the url tag in templates
# the 'name' value as called by the {% url %} template tag

urlpatterns = [
    path( "", views.index, name="index" ),
    path( "<int:question_id>/details", views.details, name="qtn_details" ),
    path( "<int:question_id>/results/", views.results, name="qtn_results" ),
    path( "<int:question_id>/vote/", views.vote, name="qtn_vote" ),
    
]
