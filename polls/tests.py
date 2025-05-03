
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
    time = timezone.now() + datetime.timedelta(days=days)
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
        
        # create a past question using helper function 
        question = create_question(question_text='Past Question', days=-30)
        
        # hit the end point
        response = self.client.get( reverse('polls:index') )
        
        # check -- the question must exist in the endpoint context data
        # self.assertQuerySetEqual( what is returned , what you expect )
        self.assertQuerySetEqual( 
            response.context['latest_questions_list'],
            [question]
        )    
    
    def test_future_question(self):
        """
        this is to test a question
        that is published in the future from now
        the question should not be in the context data
        """
        
        # create a question thats 7 days in the future
        create_question(question_text="Future Question", days=7)
        
        # request for questions list view
        response = self.client.get(reverse('polls:index'))
        
        # check the context data that comes in
        # the future question must NOT bt there hence an empty list
        self.assertQuerySetEqual(
            response.context['latest_questions_list'],
            [] # this should be empty
        )
        
    def test_future_question_and_past_question(self):
        """
        This is to test both future and past questions
        only the past question should exist in the context 
        """
        
        # add two questions with differing times, one from the past and the other from the future
        past_question = create_question(question_text="Past Question", days=-7)
        
        # for future question, we dont asssign it cause it wont show up anyway
        create_question(question_text="Future Question", days=7)
        
        # get the response from the view
        response = self.client.get(reverse('polls:index'))
        
        # confirm your results -- context must have only passed question
        self.assertQuerySetEqual(
            response.context['latest_questions_list'],
            [past_question]
        )

    def test_two_past_questions(self):
        """
        This is to test when more that one past questions exist
        Both questions should come in the context data
        Hence the index page must display both
        """
        
        # add two questions with past times
        past_question_1 = create_question(question_text="Past Question", days=-7)
        past_question_2 = create_question(question_text="Past Question", days=-10)
        
        # get the response from the view
        response = self.client.get(reverse('polls:index'))
        
        # confirm your results -- context must have BOTH questions
        self.assertQuerySetEqual(
            response.context['latest_questions_list'],
            [past_question_1, past_question_2]
        )

# testing the question details view

# considerations made
    # - user can guess future question URL and put it in the search bar and get view of future question
    #   which should not be allowed

class QuestionDetailViewTests(TestCase):
    
    def test_past_question(self):
        """
        This ensure that a question in past time can be retrived
        """
        # create a past question
        past_question = create_question(question_text='past question', days=-15)
        
        # get url to that future question detail (a would-be url)
        url = reverse(viewname="polls:qtn_details", args=(past_question.id,))
        
        # send get request with client to that end point
        response = self.client.get(url)

        #  the system should return 200 for found 
        self.assertEqual(response.status_code, 200)
        
        # check if the question text is found in the html template       
        self.assertContains(response, past_question.question_text)

    def test_future_question(self):
        """
        the detail view of a question posted in the future
        should return a 404 not found error
        """        
        # create a future question
        future_question = create_question(question_text='future question', days=10)
        
        # get url to that future question detail (a would-be url)
        url = reverse(viewname="polls:qtn_details", args=(future_question.id,))
        
        # send get request with client to that end point
        response = self.client.get(url)

        #  the system should return 404 not found 
        self.assertEqual(response.status_code, 404)
        
