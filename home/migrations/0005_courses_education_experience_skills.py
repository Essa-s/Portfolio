# Generated by Django 4.2.8 on 2024-01-30 13:57

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_profile_github'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('present', models.BooleanField()),
                ('details', models.TextField()),
                ('main_image', models.ImageField(blank=True, null=True, upload_to=home.models.project_files)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=50)),
                ('degree', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('present', models.BooleanField()),
                ('details', models.TextField()),
                ('main_image', models.ImageField(blank=True, null=True, upload_to=home.models.project_files)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('present', models.BooleanField()),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=20)),
                ('rate', models.IntegerField()),
            ],
        ),
    ]
