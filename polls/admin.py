from django.contrib import admin
from .models import Choice, Question



class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

# create an admin for the model
class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"] # flips the ordering when editting
    
    # more advanced thing to do is to use fieldsets
    fieldsets = [
        # a category of fields
        ( None, { "fields":[ "question_text" ] } ),
        
        # another category
        ( "Date Information", { 
                                "fields":[ "pub_date" ], # fields to include
                                "classes":["collapse"]  # classes (prolly styling) to include ; collapse means you can collapse/expand the category
                                } )
    ]
    inlines = [ChoiceInline]
    
# link the admin and the model
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)