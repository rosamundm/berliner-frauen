# Generated by Django 3.2.13 on 2022-05-06 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streets', '0002_auto_20220428_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='category_slug',
        ),
        migrations.RenameField(
            model_name='district',
            old_name='slug',
            new_name='district_slug',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='slug',
            new_name='person_slug',
        ),
        migrations.RenameField(
            model_name='street',
            old_name='slug',
            new_name='street_slug',
        ),
    ]
