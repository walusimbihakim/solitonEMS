# Generated by Django 2.2.2 on 2019-09-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0004_payslip_total_nssf_contrib'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip',
            name='bonus',
            field=models.IntegerField(default=0),
        ),
    ]