# Generated by Django 4.0.1 on 2022-01-28 03:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_alter_ride_arrivaltime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='arrivaltime',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 28, 3, 58, 9, 287405, tzinfo=utc)),
        ),
    ]
