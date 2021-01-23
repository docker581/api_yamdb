# Generated by Django 3.0.5 on 2021-01-23 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210123_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(choices=[(4, '4'), (1, '1'), (5, '5'), (9, '9'), (3, '3'), (10, '10'), (7, '7'), (2, '2'), (6, '6'), (8, '8'), (0, '0')], default=0),
        ),
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='media', to='api.Category'),
        ),
    ]
