# Generated by Django 4.1.6 on 2023-02-15 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_inboxmessage_alter_bookrenthistory_back_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='bookrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 17, 11, 17, 22, 151477)),
        ),
    ]
