# Generated by Django 4.2.7 on 2023-11-28 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('emailAddress', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=100)),
            ],
        ),
    ]
