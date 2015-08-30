# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django import db
from django.utils import timezone


def filling_data(apps, schema_editor):
    """
    Filling in Db default data
    """
    print type(schema_editor)
    Blog = apps.get_model('learn', 'Blog')
    if not Blog.objects.count():
        Blog.objects.bulk_create([
            Blog(name='Homer blog', tagline='Beer, donuts'),
            Blog(name='Marge blog', tagline='I\' Marge'),
            Blog(name='Bart blog', tagline='Eat my pants'),
            Blog(name='Lisa blog', tagline='My blog'),
        ])

    Author = apps.get_model('learn', 'Author')
    if not Author.objects.count():
        Author.objects.bulk_create([
            Author(name='Homer J Simpson', email='homerj@gmail.com'),
            Author(name='Marge Simpson', email='margory@gmail.com'),
            Author(name='Bart Simpson', email='elbarto@gmail.com'),
            Author(name='Lisa Simpson', email='lisas@gmail.com'),
        ])

    Entry = apps.get_model('learn', 'Entry')
    if not Entry.objects.count():
        Entry.objects.bulk_create([
            Entry(blog=Blog.objects.get(name__icontains='Homer'), headline='Homer first post',
                  body_text='Post body here!!!', pub_date=timezone.now().date(), mod_date=timezone.now().date(),
                  n_comments=0, n_pingbacks=0, rating=0),
            Entry(blog=Blog.objects.get(name__icontains='Marge'), headline='Marge first post',
                  body_text='Post body here!!!', pub_date=timezone.now().date(), mod_date=timezone.now().date(),
                  n_comments=0, n_pingbacks=0, rating=0),
            Entry(blog=Blog.objects.get(name__icontains='Bart'), headline='Bart first post',
                  body_text='Post body here!!!', pub_date=timezone.now().date(), mod_date=timezone.now().date(),
                  n_comments=0, n_pingbacks=0, rating=0),
            Entry(blog=Blog.objects.get(name__icontains='Lisa'), headline='Lisa first post',
                  body_text='Post body here!!!', pub_date=timezone.now().date(), mod_date=timezone.now().date(),
                  n_comments=0, n_pingbacks=0, rating=0),
        ])

    for blog in Blog.objects.all():
        first_name, second_name = blog.name.split(' ')
        blog.entry_set.get(headline__icontains=first_name).authors.add(Author.objects.get(name__icontains=first_name))


class Migration(migrations.Migration):
    dependencies = [
        ('learn', '0005_author_blog_entry'),
    ]

    operations = [
        migrations.RunPython(filling_data)
    ]
