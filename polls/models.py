from datetime import datetime, timedelta
from django.db import models

from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text


notes ="""

from interactive shell
using the API to play with the ORM 

# creating a query set manager
q = Question.objects.get(pk=1)

# calling on all the choices for this question
q.choice_set.all()

# creating 3 answers for this question
q.choice_set.create( choice_text = "I dont have one", votes = 0 )
q.choice_set.create( choice_text = "Girl is my name", votes = 0 )
c = q.choice_set.create( choice_text = "My name is a boy", votes = 0 )

# following relationships till what you want
Choice.objects.filter(question__pub_date__year=current_year)


# Let's delete one of the choices. Use delete() for that.
c = q.choice_set.filter(choice_text__startswith="Just hacking")
c.delete()

STUDY MORE ON ORM MANIPULATIONS


"""