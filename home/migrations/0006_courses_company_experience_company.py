# Generated by Django 4.2.8 on 2024-01-31 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_courses_education_experience_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='company',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]