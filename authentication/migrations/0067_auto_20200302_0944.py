# Generated by Django 2.2.7 on 2020-03-02 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0066_auto_20200226_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='appointment_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='contact',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='digital_address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='postal_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='region',
            field=models.CharField(choices=[('Bono East Region', 'Bono East Region'), ('Ahafo Region', 'Ahafo Region'), ('Bono Region', 'Bono Region'), ('North East Region', 'North East Region'), ('Savannah Region', 'Savannah Region'), ('Western North Region', 'Western North Region'), ('Western Region', 'Western Region'), ('Volta Region', 'Volta Region'), ('Greater Accra Region', 'Greater Accra Region'), ('Eastern Region', 'Eastern Region'), ('Ashanti Region', 'Ashanti Region'), ('Central Region', 'Central Region'), ('Northern Region', 'Northern Region'), ('Upper East Region', 'Upper East Region'), ('Upper West Region', 'Upper West Region')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='website',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
