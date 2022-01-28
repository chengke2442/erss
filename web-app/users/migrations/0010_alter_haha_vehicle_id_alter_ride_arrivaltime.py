# Generated by Django 4.0.1 on 2022-01-27 21:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_ride_arrivaltime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='haha',
            name='vehicle_id',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='arrivaltime',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 27, 21, 14, 55, 649174, tzinfo=utc)),
        ),
    ]
