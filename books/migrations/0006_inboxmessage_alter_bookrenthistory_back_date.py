# Generated by Django 4.1.6 on 2023-02-15 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_bookrenthistory_back_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='InboxMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='bookrenthistory',
            name='back_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 17, 10, 7, 56, 927703)),
        ),
    ]