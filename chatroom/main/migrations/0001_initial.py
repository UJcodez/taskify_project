# Generated by Django 4.2 on 2023-07-14 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=200)),
                ('passwrd', models.CharField(max_length=200)),
            ],
        ),
    ]