# Generated by Django 2.2.7 on 2020-02-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0056_institution_establishment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='establishment_date',
            field=models.DateField(),
        ),
    ]
