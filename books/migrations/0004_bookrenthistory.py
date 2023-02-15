# Generated by Django 3.2.12 on 2023-02-14 12:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_date', models.DateField(auto_now_add=True)),
                ('back_date', models.DateField(default=datetime.datetime(2023, 3, 16, 12, 51, 59, 296531))),
                ('book', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='books.book')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]