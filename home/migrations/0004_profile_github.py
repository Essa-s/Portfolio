# Generated by Django 4.2.8 on 2023-12-31 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_profile_fb_profile_insta_profile_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
    ]
