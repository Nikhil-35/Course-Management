# Generated by Django 3.2.12 on 2022-11-21 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_assignments_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignments',
            name='number',
        ),
    ]