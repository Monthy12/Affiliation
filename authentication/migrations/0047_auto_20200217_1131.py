# Generated by Django 2.2.7 on 2020-02-17 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0046_auto_20200217_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination_unit',
            name='quantity',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
