# Generated by Django 3.2.8 on 2021-12-09 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interventions', '0002_feedingday'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedingentries',
            name='day',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='interventions.feedingday'),
            preserve_default=False,
        ),
    ]
