# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pivx',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.FloatField()),
                ('percent_change', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='speedandweight',
            name='Gravitational_Force',
            field=models.IntegerField(max_length=350, blank=True),
        ),
        migrations.AlterField(
            model_name='speedandweight',
            name='distance_travelled',
            field=models.IntegerField(unique=True, max_length=350),
        ),
        migrations.AlterField(
            model_name='speedandweight',
            name='mass',
            field=models.IntegerField(max_length=350, blank=True),
        ),
        migrations.AlterField(
            model_name='speedandweight',
            name='speed',
            field=models.IntegerField(max_length=350, blank=True),
        ),
        migrations.AlterField(
            model_name='speedandweight',
            name='time',
            field=models.IntegerField(max_length=350, blank=True),
        ),
    ]
