# Generated by Django 5.0.6 on 2024-06-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_customeuser_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='DOB',
            field=models.DateField(),
        ),
    ]
