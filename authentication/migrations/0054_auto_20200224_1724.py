# Generated by Django 2.2.7 on 2020-02-24 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0053_accreditation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='management',
            old_name='contact',
            new_name='official_contact',
        ),
        migrations.RenameField(
            model_name='management',
            old_name='primary_contact',
            new_name='personal_contact',
        ),
    ]
