# Generated by Django 4.1.7 on 2023-04-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_skills_course_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='available_sits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='content',
            field=models.TextField(default='this is content for this course'),
            preserve_default=False,
        ),
    ]
