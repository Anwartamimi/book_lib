# Generated by Django 4.1.6 on 2023-02-16 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0023_category_name_alter_bookrenthistory_back_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AlterField(
            model_name='bookrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 18, 8, 49, 36, 915795)),
        ),
    ]
