# Generated by Django 2.2.7 on 2020-01-08 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0016_auto_20200108_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution_Head',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Institution_Head',
            },
        ),
    ]
