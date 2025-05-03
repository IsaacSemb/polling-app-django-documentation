
import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

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
    
    def create_question(question_text, days):
        """
        create a question with question text
        and a number of days off set from now
        questions in the past have to show up on the display        
        """
        time = timezone.now() = datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)
    
class QuestionIndexViewTests(TestCase):
    
    def test_no_questions(self):
        """ 
        if no questions exist
        Display an appropriate question
        """
        
        # sending a get request to the test client
        response = self.client.get( reverse('polls:index') )
        
        # checking that the request has to be accepted
        self.assertEqual( response.status_code, 200 )
        
        # checking the results of the response 
        self.assertContains(response, "No polls are available")
        
        # the query set must be empty too
        self.assertQuerySetEqual(response.context['latest_questions_list'], [])
        
        
    def test_past_question(self):
        pass
    
    def test_future_question(self):
        pass

    def test_future_question_and_past_question(self):
        pass

    def test_two_past_question(self):
        pass
