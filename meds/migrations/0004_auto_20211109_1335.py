# Generated by Django 3.2.8 on 2021-11-09 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0003_marprn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marscheduled',
            name='med',
        ),
        migrations.DeleteModel(
            name='MarPrn',
        ),
        migrations.DeleteModel(
            name='MarScheduled',
        ),
    ]
