# Generated by Django 5.1.1 on 2024-10-20 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='dropoff_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='dropoff_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='pickup_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='pickup_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
