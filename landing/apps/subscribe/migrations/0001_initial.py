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
                ('client', models.CharField(max_length=100)),
                ('account', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('coupon_used', models.CharField(max_length=100)),
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
