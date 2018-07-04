from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInLine(admin.TabularInline):
    """
    Choice objects are edited on the Question admin page.
    By default, provide enough fields for 3 extra choices.

    This way we can add multiple choices when creating a
    new question, instead of having to add a question, and
    then add its choices 1 by 1.
    
    Use TabularInline to display the objects in a compact,
    table-based format.
    """
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    """
    Customize how the admin form for Question looks and works
    """
    # split the form up into fieldsets, choose an intuitive order
    # give titles to the fieldsets
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
        ]
    inlines = [ChoiceInLine]
    # Display more fields other than just str(Question)
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Since we set this field to boolean, we can use the following filter
    list_filter = ['pub_date']
    # Add a search box, here we only search the question text
    search_fields = ['question_text']
    
# class MyAdminSite(admin.AdminSite):
#     site_header = 'Polls administration'
#     site_title = 'Polls admin page'
# 
# admin_site = MyAdminSite()
admin.site.register(Question, QuestionAdmin)