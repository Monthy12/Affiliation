# Generated by Django 2.2.7 on 2020-02-18 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0048_auto_20200217_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='programme',
            name='inst_name',
            field=models.CharField(default='test', max_length=50),
        ),
    ]
