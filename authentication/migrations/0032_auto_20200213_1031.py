# Generated by Django 2.2.7 on 2020-02-13 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0031_mentor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='first_name_department_head',
        ),
        migrations.RemoveField(
            model_name='department',
            name='last_name_department_head',
        ),
        migrations.RemoveField(
            model_name='department',
            name='other_name_department_head',
        ),
        migrations.AddField(
            model_name='department',
            name='name_department_head',
            field=models.CharField(default='test', max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='appointment_year',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='department',
            name='awarding_institution',
            field=models.CharField(default='test', max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='completion_year',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(default='test', max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='highest_qualification',
            field=models.CharField(default='test', max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='study_programme',
            field=models.CharField(default='test', max_length=100),
        ),
    ]