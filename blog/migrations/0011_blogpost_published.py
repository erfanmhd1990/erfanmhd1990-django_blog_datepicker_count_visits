# Generated by Django 3.2.12 on 2023-02-17 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_blogpost_start_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='published',
            field=models.DateField(default=datetime.date(2021, 1, 3)),
            preserve_default=False,
        ),
    ]
