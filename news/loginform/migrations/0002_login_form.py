# Generated by Django 4.0.2 on 2022-05-08 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='login_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('create_password', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
    ]
