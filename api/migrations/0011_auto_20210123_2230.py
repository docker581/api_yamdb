# Generated by Django 3.0.5 on 2021-01-23 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210123_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(choices=[(10, '10'), (8, '8'), (9, '9'), (2, '2'), (7, '7'), (4, '4'), (0, '0'), (1, '1'), (6, '6'), (3, '3'), (5, '5')], default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='title_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Title'),
        ),
    ]
