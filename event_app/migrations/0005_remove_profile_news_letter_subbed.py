# Generated by Django 3.2.6 on 2021-09-15 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0004_newsletter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='news_letter_subbed',
        ),
    ]
