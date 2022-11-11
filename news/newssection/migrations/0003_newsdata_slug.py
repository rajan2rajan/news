# Generated by Django 4.0.2 on 2022-05-14 09:09

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newssection', '0002_alter_newsdata_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsdata',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
