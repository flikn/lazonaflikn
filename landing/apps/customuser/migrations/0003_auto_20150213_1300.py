# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0002_myuser_was_subscribed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='subscriptor',
            field=models.ForeignKey(blank=True, to='subscribe.Subscriptor', null=True),
            preserve_default=True,
        ),
    ]
