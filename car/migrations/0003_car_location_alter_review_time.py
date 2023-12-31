# Generated by Django 4.1.4 on 2023-02-02 05:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_car_is_avaliable_alter_car_comment_alter_car_feature_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='location',
            field=models.CharField(choices=[('M', 'Mumbai'), ('D', 'Delhi'), ('B', 'Bangalore'), ('H', 'Hyderabad'), ('A', 'Ahmedabad'), ('C', 'Chennai'), ('K', 'Kolkata'), ('S', 'Surat'), ('V', 'Vadodara'), ('P', 'Pune'), ('J', 'Jaipur'), ('L', 'Lucknow')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 2, 11, 2, 26, 234820)),
        ),
    ]
