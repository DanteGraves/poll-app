# Import section.
from django.contrib import admin
from .models import Question, Choice

# Create classes.
class ChoiceInline(admin.TabularInline):
    """
    Defines an inline admin interface for the Choice model.
    This allows choices to be edited directly within the Question admin interface.
    """
    model = Choice
    extra = 3  

class QuestionAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Question model.
    """
    # Specifies the fields to be displayed in the form, grouped into fieldsets.
    fieldsets = [
        (None, {'fields': ['question_text']}),  
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),  
    ]
    inlines = [ChoiceInline]  
    list_display = ('question_text', 'pub_date', 'was_published_recently')  
    list_filter = ['pub_date'] 
    search_fields = ['question_text']  

# Registers the Question model with the custom QuestionAdmin configuration.
admin.site.register(Question, QuestionAdmin)
