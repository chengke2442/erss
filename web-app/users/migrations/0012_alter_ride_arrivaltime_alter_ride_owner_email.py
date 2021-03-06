# Generated by Django 4.0.1 on 2022-01-28 00:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_ride_arrivaltime_alter_ride_owner_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='arrivaltime',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 28, 0, 45, 30, 458921, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ride',
            name='owner_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
