# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HaveShirt',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('belongingTeam', models.IntegerField(default=0)),
                ('size', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('manager_name', models.CharField(max_length=20)),
                ('team_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WantShirt',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('belongingTeam', models.IntegerField(default=0)),
                ('size', models.CharField(max_length=3)),
                ('requestingTeam', models.ForeignKey(to='shirtmanager.Team')),
            ],
        ),
        migrations.AddField(
            model_name='haveshirt',
            name='owningTeam',
            field=models.ForeignKey(to='shirtmanager.Team'),
        ),
    ]
