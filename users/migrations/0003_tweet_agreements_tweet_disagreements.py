# Generated by Django 4.1.13 on 2024-02-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_tweet_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='agreements',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='disagreements',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
