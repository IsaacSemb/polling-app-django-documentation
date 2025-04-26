from django.urls import path
from . import views

urlpatterns = [
    path( "", views.index, name="index" ),
    path( "<int:question_id>/", views.details, name="qtn_details" ),
    path( "<int:question_id>/results/", views.results, name="qtn_results" ),
    path( "<int:question_id>/vote/", views.vote, name="qtn_vote" ),
    
]
