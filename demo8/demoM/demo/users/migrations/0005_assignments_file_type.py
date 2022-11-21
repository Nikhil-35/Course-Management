# Generated by Django 3.2.12 on 2022-11-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_assignments_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignments',
            name='file_type',
            field=models.CharField(choices=[('.zip', '.zip'), ('.tgz', '.tgz'), ('.cpp', '.cpp'), ('.py', '.py')], default='.zip', max_length=20),
        ),
    ]
