# Generated by Django 4.1.6 on 2023-02-15 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_alter_bookrenthistory_back_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 17, 13, 57, 13, 823798)),
        ),
    ]