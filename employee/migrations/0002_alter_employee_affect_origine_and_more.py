# Generated by Django 5.0.1 on 2024-02-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='affect_origine',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_detach',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_recrut',
            field=models.DateField(),
        ),
    ]
