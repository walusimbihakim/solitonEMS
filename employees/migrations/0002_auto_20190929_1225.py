# Generated by Django 2.2.2 on 2019-09-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='lunch_allowance',
            field=models.IntegerField(default=150000, max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='basic_salary',
            field=models.IntegerField(max_length=10),
        ),
    ]