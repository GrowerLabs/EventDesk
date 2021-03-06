# Generated by Django 3.2.6 on 2021-10-13 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0012_chat_chatroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_app.event')),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_app.profile')),
            ],
        ),
    ]
