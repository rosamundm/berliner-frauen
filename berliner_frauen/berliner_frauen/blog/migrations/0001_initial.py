# Generated by Django 3.2.19 on 2023-06-26 20:03

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('published', models.DateField()),
                ('body', tinymce.models.HTMLField(blank=True, null=True)),
            ],
        ),
    ]