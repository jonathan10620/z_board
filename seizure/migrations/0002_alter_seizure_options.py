# Generated by Django 3.2.8 on 2021-12-09 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seizure', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seizure',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Seizures'},
        ),
    ]
