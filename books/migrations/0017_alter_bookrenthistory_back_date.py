# Generated by Django 4.1.6 on 2023-02-16 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_alter_bookrenthistory_back_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 18, 8, 22, 28, 311424)),
        ),
    ]
