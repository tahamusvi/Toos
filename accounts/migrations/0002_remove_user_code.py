# Generated by Django 3.2.8 on 2022-03-04 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='code',
        ),
    ]
