# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0006_filling_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to=b'blog_logo', verbose_name=b'blog_logo', blank=True),
        ),
    ]
