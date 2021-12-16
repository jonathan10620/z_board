# Generated by Django 3.2.8 on 2021-12-12 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interventions', '0005_feedingentries_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedingentries',
            name='date',
        ),
        migrations.AddField(
            model_name='feedingentries',
            name='isoweek',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]