# Generated by Django 4.0.1 on 2022-01-28 04:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_alter_ride_arrivaltime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='driver_id',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='arrivaltime',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 28, 4, 2, 41, 772558, tzinfo=utc)),
        ),
    ]