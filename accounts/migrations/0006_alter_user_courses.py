# Generated by Django 3.2.8 on 2022-03-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0054_onlineclass'),
        ('accounts', '0005_alter_user_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='user', to='course.Course'),
        ),
    ]
