# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=50, verbose_name=b'email address')),
                ('username', models.CharField(max_length=50, blank=True)),
                ('first_name', models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z ]', b'Invalid name.')])),
                ('last_name', models.CharField(blank=True, max_length=255, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z ]', b'Invalid name.')])),
                ('is_admin', models.BooleanField(default=False)),
                ('was_registered', models.BooleanField(default=False)),
                ('raw_password', models.CharField(max_length=100, null=True, blank=True)),
                ('subscriptor', models.ForeignKey(to='subscribe.Subscriptor', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
