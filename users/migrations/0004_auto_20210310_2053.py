# Generated by Django 3.1 on 2021-03-11 02:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210310_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='uploadDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 11, 2, 53, 32, 55010, tzinfo=utc)),
        ),
    ]
