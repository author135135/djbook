from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_per_page = 20
    fieldsets = [
        ('Content', {'fields': ['question_text'], 'classes': ['content-fieldset']}),
        ('Date Setting', {'fields': ['pub_date'], 'classes': ['date-fieldset']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
