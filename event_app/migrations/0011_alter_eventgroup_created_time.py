# Generated by Django 3.2.6 on 2021-10-12 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0010_eventgroup_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventgroup',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
