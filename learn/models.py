from django.db import models
from django.contrib import admin
from django.utils import timezone


class Person(models.Model):
    POSITIONS = (
        ('j_py', 'Python junior developer'),
        ('m_py', 'Python middle developer'),
        ('s_py', 'Python senior developer'),
        ('j_js', 'Javascript junior developer'),
        ('m_js', 'Javascript middle developer'),
        ('s_js', 'Javascript senior developer'),
        ('j_php', 'PHP junior developer'),
        ('m_php', 'PHP middle developer'),
        ('s_php', 'PHP senior developer'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.ForeignKey('Company', blank=True, null=True, related_name='persons')
    position = models.CharField(max_length=255, choices=POSITIONS)
    recruitment = models.DateField(default=timezone.now)
    retirement = models.DateField(blank=True, null=True, name='leaving work')

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        db_table = 'person'
        verbose_name_plural = 'persons'


class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'company', 'position']
    list_filter = ['company', 'position', 'recruitment']


class Company(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    founding_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'company'
        verbose_name_plural = 'companies'


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']


class Tasks(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    allotted_time = models.IntegerField()
    elapsed_time = models.IntegerField()
    created = models.DateTimeField(default=timezone.now)
    closed = models.DateTimeField(blank=True, null=True)
    persons = models.ManyToManyField(Person, related_name='persons', db_table='tasks_to_persons')

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'tasks'
        verbose_name_plural = 'tasks'


class TasksAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'deadline']
    list_filter = ['created', 'deadline']


admin.site.register(Person, PersonAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Tasks, TasksAdmin)
