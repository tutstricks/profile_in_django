# Generated by Django 2.1.15 on 2021-03-18 08:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210318_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media/users'),
        ),
        migrations.AlterField(
            model_name='userfile',
            name='uploadDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 18, 8, 12, 34, 659306, tzinfo=utc)),
        ),
    ]
