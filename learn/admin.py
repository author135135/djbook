from django.contrib import admin
from learn import models

"""
class PersonNoteInline(admin.StackedInline):
    model = models.PersonNote


class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'company', 'position']
    list_filter = ['company', 'position', 'recruitment']

    inlines = [PersonNoteInline]
"""


class CompanyAdmin(admin.ModelAdmin):
    ordering = ['-founding_date']
    list_display = ['name', 'founding_date']


class TasksAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'deadline']
    list_filter = ['created', 'deadline']


class PersonNoteAdmin(admin.ModelAdmin):
    list_display = ['get_person', 'title']

    def get_person(self, obj):
        return '%s %s' % (obj.first_name, obj.last_name)

    get_person.short_description = 'Person name'


class BlogAdmin(admin.ModelAdmin):
    list_display = ['name']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


class EntryAdmin(admin.ModelAdmin):
    list_display = ['headline', 'pub_date', 'get_authors']

    def get_authors(self, obj):
        return ", ".join(map(unicode, obj.authors.all()))

    get_authors.short_description = 'Post authors'


# admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Tasks, TasksAdmin)
admin.site.register(models.PersonNote, PersonNoteAdmin)
admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Entry, EntryAdmin)
