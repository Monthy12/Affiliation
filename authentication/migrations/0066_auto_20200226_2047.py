# Generated by Django 2.2.7 on 2020-02-26 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0065_auto_20200226_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_details',
            name='registration_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='datetime',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='datetime',
            field=models.DateField(auto_now=True),
        ),
    ]
