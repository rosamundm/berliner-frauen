# Generated by Django 3.2.19 on 2023-06-25 15:02

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('streets', '0005_district_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='street',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
