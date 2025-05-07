from django.contrib import admin
from .models import Question


# create an admin for the model
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"] # flips the ordering when editting
    
# link the admin and the model
admin.site.register(Question, QuestionAdmin)
