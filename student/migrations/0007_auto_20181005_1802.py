# Generated by Django 2.1.1 on 2018-10-05 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_internship_project_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='rate',
            field=models.IntegerField(),
        ),
    ]
