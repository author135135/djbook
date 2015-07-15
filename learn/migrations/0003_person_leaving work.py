# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_person_recruitment'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='leaving work',
            field=models.DateField(null=True, blank=True),
        ),
    ]
