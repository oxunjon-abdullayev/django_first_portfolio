# Generated by Django 4.2.1 on 2023-07-15 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=155)),
                ('email', models.CharField(max_length=155)),
                ('text', models.TextField()),
            ],
        ),
    ]
