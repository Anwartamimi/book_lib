# Generated by Django 4.1.6 on 2023-02-16 09:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0025_category_nameofcategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='nameofcategory',
        ),
        migrations.AlterField(
            model_name='bookrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2023, 2, 23, 9, 28, 45, 475135)),
        ),
    ]