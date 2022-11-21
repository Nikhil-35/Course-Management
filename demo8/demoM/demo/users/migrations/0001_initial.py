# Generated by Django 4.1.2 on 2022-11-21 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignmentfile', models.FileField(upload_to='uploads/')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('deadline', models.DateTimeField()),
                ('upload_type', models.CharField(choices=[('.zip', '.zip'), ('.tgz', '.tgz'), ('.cpp', '.cpp'), ('.py', '.py')], default='.zip', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('assignments', models.ManyToManyField(to='users.assignments')),
            ],
        ),
        migrations.CreateModel(
            name='studentsubmissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('solution', models.FileField(upload_to='uploads/')),
                ('file_name', models.CharField(default='x', max_length=300)),
                ('feedback', models.CharField(max_length=300)),
                ('marks', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='pending', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=100)),
                ('identity', models.CharField(choices=[('teacher', 'teacher'), ('student', 'student'), ('assistant', 'assistant')], default='student', max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('roll_no', models.CharField(max_length=9, unique=True)),
                ('courses_registered', models.ManyToManyField(default='', to='users.courses')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='u', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='assignments',
            name='s',
            field=models.ManyToManyField(to='users.studentsubmissions'),
        ),
    ]
