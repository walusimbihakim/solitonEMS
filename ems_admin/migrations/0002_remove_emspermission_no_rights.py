# Generated by Django 3.0 on 2020-02-07 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ems_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emspermission',
            name='no_rights',
        ),
    ]