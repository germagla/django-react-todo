# Generated by Django 3.2.3 on 2021-05-29 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='owner',
        ),
    ]
