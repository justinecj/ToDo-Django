# Generated by Django 4.2.6 on 2023-10-24 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='date',
            field=models.DateField(default=datetime.date(2023, 10, 24)),
        ),
    ]
