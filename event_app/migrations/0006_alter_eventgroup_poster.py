# Generated by Django 3.2.6 on 2021-09-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0005_remove_profile_news_letter_subbed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgroup',
            name='poster',
            field=models.ImageField(default='group_banner.png', upload_to='group_posters'),
        ),
    ]
