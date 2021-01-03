# Generated by Django 3.1.3 on 2021-01-02 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0015_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master_data.company'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master_data.country'),
        ),
    ]