# Generated by Django 5.0.4 on 2024-04-15 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('short_name', models.CharField(max_length=128)),
                ('official_name', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=256)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('altitude', models.SmallIntegerField(blank=True)),
                ('url', models.URLField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('short_name', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('birthdate', models.DateField()),
                ('nationality', models.CharField(max_length=256)),
                ('url', models.URLField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('year', models.PositiveSmallIntegerField()),
                ('round', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=256)),
                ('date', models.DateField()),
                ('url', models.URLField(max_length=256)),
                ('circuit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='races', to='stats.circuit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DriverStanding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveSmallIntegerField()),
                ('position', models.PositiveSmallIntegerField()),
                ('wins', models.PositiveSmallIntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='standings', to='stats.driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='driver_standings', to='stats.race')),
            ],
        ),
    ]
