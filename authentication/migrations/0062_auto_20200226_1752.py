# Generated by Django 2.2.7 on 2020-02-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0061_auto_20200226_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='establishment_date',
            field=models.DateTimeField(null=True),
        ),
    ]