# Generated by Django 3.2.8 on 2022-04-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0011_alter_receipt_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='code',
            field=models.DecimalField(decimal_places=0, max_digits=5, unique=True),
        ),
    ]