# Generated by Django 2.2.1 on 2019-07-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_holidays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidays',
            name='duration',
            field=models.CharField(max_length=15),
        ),
    ]
