# Generated by Django 3.0.5 on 2021-01-23 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210123_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(choices=[(4, '4'), (7, '7'), (0, '0'), (10, '10'), (3, '3'), (2, '2'), (9, '9'), (8, '8'), (5, '5'), (6, '6'), (1, '1')], default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='title_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.GenreTitle'),
        ),
    ]