# Generated by Django 3.2.12 on 2023-02-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_published'),
        ),
    ]
