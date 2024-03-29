# Generated by Django 5.0 on 2024-02-04 15:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='name',
        ),
        migrations.RemoveField(
            model_name='department',
            name='wikipedia_link',
        ),
        migrations.AddField(
            model_name='department',
            name='courses',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapp.department')),
            ],
        ),
        migrations.DeleteModel(
            name='FormSubmission',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
