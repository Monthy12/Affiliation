# Generated by Django 2.2.7 on 2020-02-12 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0024_auto_20200212_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution_type',
            name='user',
        ),
        migrations.AddField(
            model_name='institution_type',
            name='institution',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.Institution'),
        ),
        migrations.AlterField(
            model_name='institution_type',
            name='type',
            field=models.CharField(default='test', max_length=100, null=True),
        ),
    ]
