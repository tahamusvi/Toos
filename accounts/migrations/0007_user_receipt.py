# Generated by Django 3.2.8 on 2022-04-19 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0009_receipt'),
        ('accounts', '0006_alter_user_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='receipt',
            field=models.ManyToManyField(blank=True, related_name='user', to='stuff.Receipt'),
        ),
    ]
