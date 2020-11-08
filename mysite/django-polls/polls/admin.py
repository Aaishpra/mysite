from django.contrib import admin

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields = [(None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date''was_published_recently')
    list_filter = ['pub_date']

class ChoiceInline(admin.TabularInline):
    #...

admin.site.register(Question, QuestionAdmin)    
# Register your models here.
