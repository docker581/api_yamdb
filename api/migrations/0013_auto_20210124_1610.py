# Generated by Django 3.0.5 on 2021-01-24 13:10

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210124_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=api.models.IntegerRangeField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='title_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.Title'),
        ),
    ]