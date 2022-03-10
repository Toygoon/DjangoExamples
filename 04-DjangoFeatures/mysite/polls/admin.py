from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    # Change field sequences
    fields = ['pub_date', 'question_text']
    # Show separated fields
    fieldsets = [
        ('Question Statement', {'fields' : ['quesiton_text']}),
        ('Date Information', {
            'fields' : ['pub_date'],
            'classes' : ['collapse']}),
    ]
    
class ChoiceInline(admin.TabularInline):
    model = Choice
    # Set how many empty fields are showed
    extra = 2
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['question_text']}),
        ('Date information', {
            'fields' : ['pub_date'],
            'classes' : ['collapse'],
        })
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)