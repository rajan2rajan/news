# Generated by Django 4.0.2 on 2022-05-09 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginform', '0002_login_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='login_form',
            name='news_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='news/'),
        ),
    ]