# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=255, choices=[(b'j_py', b'Python junior developer'), (b'm_py', b'Python middle developer'), (b's_py', b'Python senior developer'), (b'j_js', b'Javascript junior developer'), (b'm_js', b'Javascript middle developer'), (b's_js', b'Javascript senior developer'), (b'j_php', b'PHP junior developer'), (b'm_php', b'PHP middle developer'), (b's_php', b'PHP senior developer')])),
            ],
            options={
                'db_table': 'person',
                'verbose_name_plural': 'persons',
            },
        ),
    ]
