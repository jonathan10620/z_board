# Generated by Django 3.2.8 on 2021-10-14 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrnMed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dose', models.CharField(max_length=200)),
                ('indication', models.CharField(max_length=200)),
            ],
        ),
    ]
