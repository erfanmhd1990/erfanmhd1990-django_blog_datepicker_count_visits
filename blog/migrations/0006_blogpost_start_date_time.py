# Generated by Django 3.2.12 on 2023-02-16 20:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpost_date_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='start_date_time',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='2017-01-01 00:00:00'),
            preserve_default=False,
        ),
    ]
