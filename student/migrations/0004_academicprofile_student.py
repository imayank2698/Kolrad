# Generated by Django 2.1.1 on 2018-10-05 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_academicprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicprofile',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]
