# Generated by Django 3.1.3 on 2020-12-30 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0005_city_country_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='country_id',
        ),
    ]