
# a mental map for how field sets are governed in django
# 


field_set = [
    
    # tuples of all the groupings
    
        # title of category              DICT THAT MAPS FIELDS TO ARRAY OF ACTUAL FIELDS
    ( "title of the category of fields": { "fields": [ "ACTUAL FIELDS" ] } ),
    
    # ANOTHER GROUPING
    (),
    
    (),
    
    (),
    
    () 

    
    
    
]

# Fundamental to remember: 
# The admin site reflects your models, 
# but fieldsets lets you control 
# how those fields show up in a structured, user-friendly way.

each_fieldsets_inside_fieldsets = (
                                    "Label for section",{
                                                            "fields": ["list of fields in that section"]
                                                        }
                                    )