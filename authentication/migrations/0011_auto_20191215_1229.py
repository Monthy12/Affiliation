# Generated by Django 2.2.7 on 2019-12-15 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_business_details_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution_type',
            name='type',
            field=models.CharField(default='test', max_length=50, null=True),
        ),
    ]