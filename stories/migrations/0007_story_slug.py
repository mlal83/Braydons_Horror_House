# Generated by Django 4.2.10 on 2024-03-15 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_profile_bio_profile_facebook_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='slug',
            field=models.SlugField(default='default-slug', unique=True),
            preserve_default=False,
        ),
    ]
