# Generated by Django 3.1.3 on 2020-12-30 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0011_company_company_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='plant_code',
            field=models.CharField(default='FU1', max_length=30),
        ),
    ]
