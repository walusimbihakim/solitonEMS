# Generated by Django 2.2.2 on 2019-07-08 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payroll',
            old_name='meal_allowance',
            new_name='paye',
        ),
    ]