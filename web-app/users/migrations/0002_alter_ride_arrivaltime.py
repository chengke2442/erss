# Generated by Django 4.0.1 on 2022-01-27 12:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='arrivaltime',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 27, 12, 43, 13, 74250, tzinfo=utc)),
        ),
    ]
