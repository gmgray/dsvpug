# Generated by Django 2.1.4 on 2018-12-10 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='srq',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 14, 35, 38, 549214)),
        ),
    ]