# Generated by Django 2.1.15 on 2021-03-18 19:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0022_auto_20210318_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 18, 19, 16, 2, 439119, tzinfo=utc)),
        ),
    ]
