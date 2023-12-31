# Generated by Django 4.1.4 on 2023-02-02 05:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_avaliable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='comment',
            field=models.ManyToManyField(blank=True, null=True, to='car.review'),
        ),
        migrations.AlterField(
            model_name='car',
            name='feature',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car', to='car.features'),
        ),
        migrations.AlterField(
            model_name='car',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='car', to='car.images'),
        ),
        migrations.AlterField(
            model_name='review',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 2, 10, 53, 54, 301011)),
        ),
    ]
