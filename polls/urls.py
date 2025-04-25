from django.urls import path
from . import views

urlpatterns = [
    path( "", views.index, name="index" ),
    path( "<int:question_id>/", views.index, name="index" ),
    path( "<int:question_id>/results", views.index, name="qtn_results" ),
    path( "<int:question_id>/vote", views.index, name="qtn_vote" ),
    
]
