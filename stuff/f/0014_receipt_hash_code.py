# Generated by Django 3.2.8 on 2022-05-16 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0013_auto_20220515_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='Hash_code',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]