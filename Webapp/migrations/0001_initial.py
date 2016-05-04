# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='speedandweight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.IntegerField(blank=True)),
                ('weight', models.IntegerField(blank=True)),
                ('Gravitational_Force', models.CharField(max_length=350, blank=True)),
                ('mass', models.CharField(max_length=350, blank=True)),
                ('time', models.CharField(max_length=350, blank=True)),
                ('distance_travelled', models.CharField(unique=True, max_length=350)),
                ('speed', models.CharField(max_length=350, blank=True)),
            ],
        ),
    ]
