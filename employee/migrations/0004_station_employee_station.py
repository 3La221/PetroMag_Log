# Generated by Django 5.0.1 on 2024-02-10 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_nbr_enfant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('wilaya', models.CharField(max_length=100)),
                ('zone', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='employee.station'),
        ),
    ]