# Generated by Django 5.1.1 on 2025-01-27 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GTA', '0006_std_form_delete_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='std_form',
            name='enrollmentNumber',
            field=models.TextField(unique=True),
        ),
    ]
