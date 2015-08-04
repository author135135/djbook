from django.db import models
from django.utils import timezone
from learn import fields


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


class PersonProxy(Person):
    class Meta:
        proxy = True


class Company(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    founding_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        print "Add new company `%s`" % self.name
        super(Company, self).save(*args, **kwargs)

    def _is_old_company(self):
        return self.founding_date < timezone.datetime(2000, 1, 1).date()

    is_old_company = property(_is_old_company)

    class Meta:
        db_table = 'company'
        verbose_name_plural = 'companies'


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


class PersonNote(Person):
    title = models.CharField(max_length=75)
    note = models.TextField(help_text="Note about person")

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'person_note'
        verbose_name_plural = 'persons notes'


class HomerBlogManager(models.Manager):
    def get_queryset(self):
        return super(HomerBlogManager, self).get_queryset().filter(name__icontains='Homer')


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    image = models.ImageField(verbose_name='blog_logo', upload_to='blog_logo', blank=True)

    objects = models.Manager()
    homer = HomerBlogManager()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse

        return reverse('learn:detail', kwargs={'blog_id': self.id})

    class Meta:
        db_table = 'blog'
        ordering = ['name']


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'author'
        ordering = ['name']


class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __unicode__(self):
        return self.headline

    class Meta:
        db_table = 'blog_entry'
