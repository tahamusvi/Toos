# Generated by Django 3.2.8 on 2022-02-25 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0003_stuff_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuff',
            name='teacher',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]