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
    company = models.ForeignKey('Company')
    position = models.CharField(max_length=255, choices=POSITIONS)
    recruitment = models.DateField(default='django.utils.timezone.now')
    retirement = models.DateField(blank=True, null=True, name='leaving work')

    def __unicode__(self):
        return "%s %s work at %s" % (self.first_name, self.last_name, self.get_position_display())

    class Meta:
        db_table = 'person'
        verbose_name_plural = 'persons'


class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'position']
    list_filter = ['position', 'recruitment']


class Company(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()


admin.site.register(Person, PersonAdmin)
