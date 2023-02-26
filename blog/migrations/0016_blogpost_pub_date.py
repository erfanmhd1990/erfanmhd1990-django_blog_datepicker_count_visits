# Generated by Django 3.0.8 on 2023-02-24 09:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_blogpost_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 24, 9, 6, 28, 933095, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]