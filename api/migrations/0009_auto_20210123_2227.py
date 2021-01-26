# Generated by Django 3.0.5 on 2021-01-23 22:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210123_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(choices=[(9, '9'), (1, '1'), (0, '0'), (4, '4'), (7, '7'), (10, '10'), (5, '5'), (3, '3'), (6, '6'), (2, '2'), (8, '8')], default=0),
        ),
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Category'),
        ),
    ]
