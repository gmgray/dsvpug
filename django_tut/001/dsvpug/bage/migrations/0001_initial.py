# Generated by Django 2.1.4 on 2018-12-10 13:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Srq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestor', models.CharField(max_length=20)),
                ('site', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('added', models.DateTimeField(default=datetime.datetime(2018, 12, 10, 14, 28, 36, 793313))),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('descrption', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='srq',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bage.Status'),
        ),
    ]