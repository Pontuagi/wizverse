# Generated by Django 4.1.13 on 2024-02-23 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.TextField(default='', max_length=300),
        ),
    ]
