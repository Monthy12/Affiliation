# Generated by Django 2.2.7 on 2020-01-30 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0021_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliation',
            name='affiliate_level',
            field=models.CharField(default='test', max_length=50),
        ),
        migrations.AddField(
            model_name='affiliation',
            name='affiliate_programme',
            field=models.CharField(default='test', max_length=100),
        ),
        migrations.AlterField(
            model_name='affiliation',
            name='affiliate_name',
            field=models.CharField(default='test', max_length=100),
        ),
    ]
