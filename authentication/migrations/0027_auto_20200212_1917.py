# Generated by Django 2.2.7 on 2020-02-12 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0026_auto_20200212_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution_type',
            name='institution',
        ),
        migrations.AddField(
            model_name='institution_type',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='institution',
            name='region',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
