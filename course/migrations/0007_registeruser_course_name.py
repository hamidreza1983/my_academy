# Generated by Django 4.1.7 on 2023-04-21 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_registeruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeruser',
            name='course_name',
            field=models.CharField(default=None, max_length=120),
            preserve_default=False,
        ),
    ]
