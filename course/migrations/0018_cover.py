# Generated by Django 3.2.8 on 2022-02-03 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_alter_soal_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]