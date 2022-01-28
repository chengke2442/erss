# Generated by Django 4.0.1 on 2022-01-28 03:35

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_relation_r_owner_id_alter_ride_arrivaltime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='driver_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.haha'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='arrivaltime',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 28, 3, 35, 57, 372436, tzinfo=utc)),
        ),
    ]