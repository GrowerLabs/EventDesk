# Generated by Django 3.2.6 on 2021-09-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0003_profile_news_letter_subbed'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
