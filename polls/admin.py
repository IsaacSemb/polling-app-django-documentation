from django.contrib import admin
from .models import Choice, Question



class ChoiceInline(admin.TabularInline):
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
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = [ "pub_date" ]
    search_fields = ["question_text"]
    
# link the admin and the model
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)