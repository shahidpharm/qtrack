# Generated by Django 3.1.3 on 2020-12-30 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_data', '0014_auto_20201230_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=50)),
                ('department_code', models.CharField(max_length=15)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_data.company')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_data.plant')),
            ],
        ),
    ]