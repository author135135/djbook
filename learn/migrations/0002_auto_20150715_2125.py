# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('deadline', models.DateField()),
                ('allotted_time', models.IntegerField()),
                ('elapsed_time', models.IntegerField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('closed', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'tasks',
                'verbose_name_plural': 'tasks',
            },
        ),
        migrations.AlterField(
            model_name='person',
            name='company',
            field=models.ForeignKey(related_name='persons', blank=True, to='learn.Company', null=True),
        ),
        migrations.AddField(
            model_name='tasks',
            name='persons',
            field=models.ManyToManyField(related_name='persons', db_table=b'tasks_to_persons', to='learn.Person'),
        ),
    ]
