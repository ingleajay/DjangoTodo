# Generated by Django 3.2.4 on 2021-06-09 18:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0002_addtask_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtask',
            name='Date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
