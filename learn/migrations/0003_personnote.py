# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_auto_20150715_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonNote',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='learn.Person')),
                ('title', models.CharField(max_length=75)),
                ('note', models.TextField()),
            ],
            options={
                'db_table': 'person_note',
                'verbose_name_plural': 'persons notes',
            },
            bases=('learn.person',),
        ),
    ]
