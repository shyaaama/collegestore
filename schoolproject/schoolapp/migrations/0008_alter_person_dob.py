# Generated by Django 5.0 on 2024-02-06 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0007_person_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dob',
            field=models.DateField(),
        ),
    ]
