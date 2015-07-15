# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='recruitment',
            field=models.DateField(default=datetime.date(2015, 7, 15)),
        ),
    ]
