from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    # Change field sequences
    fields = ['pub_date', 'question_text']
    # Show separated fields
    fieldsets = [
        ('Question Statement', {'fields' : ['quesiton_text']}),
        ('Date Information', {'fields' : ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)