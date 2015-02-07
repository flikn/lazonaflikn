# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriptor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.BigIntegerField()),
                ('account', models.BigIntegerField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('lifetime', models.PositiveSmallIntegerField(default=3)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'subscriptor',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='subscriptor',
            unique_together=set([('client', 'account')]),
        ),
        migrations.AlterIndexTogether(
            name='subscriptor',
            index_together=set([('client', 'account')]),
        ),
    ]
