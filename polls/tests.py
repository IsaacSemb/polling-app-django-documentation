
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_questions(self):
        """
        Ensuring that the 
        was_published_recently() function 
        returns False for question published in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs( future_question.was_published_recently(), False )
        
    def test_was_published_recently_with_recent_question(self):
        """
        Ensuring that the 
        was_published_recently() function 
        returns True 
        for question published with in one day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs( recent_question.was_published_recently(), True )
        
    def test_was_published_recently_with_old_question(self):
        """
        Ensuring that the 
        was_published_recently() function 
        returns True 
        for question published with in one day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        recent_question = Question(pub_date=time)
        self.assertIs( recent_question.was_published_recently(), False )
        
        
        
