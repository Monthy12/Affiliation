# Generated by Django 2.2.7 on 2020-02-12 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0023_auto_20200130_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='region',
            field=models.CharField(choices=[('Bono East Region', 'Bono East Region'), ('Ahafo Region', 'Ahafo Region'), ('Bono Region', 'Bono Region'), ('North East Region', 'North East Region'), ('Savannah Region', 'Savannah Region'), ('Western North Region', 'Western North Region'), ('Western Region', 'Western Region'), ('Volta Region', 'Volta Region'), ('Greater Accra Region', 'Greater Accra Region'), ('Eastern Region', 'Eastern Region'), ('Ashanti Region', 'Ashanti Region'), ('Central Region', 'Central Region'), ('Northern Region', 'Northern Region'), ('Upper East Region', 'Upper East Region'), ('Upper West Region', 'Upper West Region')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='town',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='institution_type',
            name='type',
            field=models.CharField(default='test', max_length=100),
        ),
    ]
