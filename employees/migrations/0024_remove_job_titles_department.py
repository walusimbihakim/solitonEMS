# Generated by Django 2.2.1 on 2019-07-12 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0023_auto_20190712_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_titles',
            name='department',
        ),
    ]
