# Generated by Django 3.2.8 on 2021-11-09 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meds', '0004_auto_20211109_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarScheduled',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given', models.BooleanField(default=False)),
                ('mar_date', models.DateField()),
                ('time', models.CharField(max_length=200)),
                ('nurse', models.CharField(max_length=20)),
                ('med', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meds.scheduledmed')),
            ],
        ),
        migrations.CreateModel(
            name='MarPrn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mar_datetime', models.DateTimeField()),
                ('initial', models.CharField(max_length=20)),
                ('indication', models.CharField(max_length=200)),
                ('med', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meds.prnmed')),
            ],
        ),
    ]
