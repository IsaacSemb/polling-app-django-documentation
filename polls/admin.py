from django.contrib import admin
from .models import Choice, Question


# create an admin for the model
class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"] # flips the ordering when editting
    
    # more advanced thing to do is to use fieldsets
    fieldsets = [
        ( None, { "fields":[ "question_text" ] } ),
        ( "Date Information", { "fields":[ "pub_date" ] } )
    ]
    
# link the admin and the model
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)