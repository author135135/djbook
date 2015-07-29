# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_personnote'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonProxy',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('learn.person',),
        ),
        migrations.AlterField(
            model_name='personnote',
            name='note',
            field=models.TextField(help_text=b'Note about person'),
        ),
    ]
