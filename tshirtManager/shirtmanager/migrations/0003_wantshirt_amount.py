# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shirtmanager', '0002_haveshirt_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='wantshirt',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
