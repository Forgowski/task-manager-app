# Generated by Django 4.1.7 on 2023-07-20 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateField(default=datetime.date(2023, 7, 20)),
        ),
    ]
