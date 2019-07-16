# Generated by Django 2.0.13 on 2019-06-25 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_auto_20190624_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('year_completed', models.CharField(max_length=4)),
                ('grade', models.CharField(max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
            ],
        ),
    ]