# Generated by Django 3.2.4 on 2021-06-09 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO', '0003_addtask_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtask',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
