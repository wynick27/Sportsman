# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='SportsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sportstype_text', models.CharField(default=b'GYM', max_length=200, choices=[(b'RC', b'Rock Climbing'), (b'TNS', b'Tennis'), (b'SWM', b'Swimming'), (b'SKI', b'Skii'), (b'BSKB', b'Basketball'), (b'SCC', b'Soccer'), (b'GYM', b'Gym'), (b'BSB', b'Baseball'), (b'BDMT', b'Badminton'), (b'ICHC', b'Ice Hockey'), (b'GLF', b'Golf'), (b'FTB', b'Football'), (b'FSH', b'Fishing'), (b'TBTN', b'Table Tennis')])),
                ('votes', models.IntegerField(default=0)),
                ('query', models.ForeignKey(to='sportsman_app.Query')),
            ],
        ),
    ]
