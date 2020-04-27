# Generated by Django 2.1.1 on 2018-10-05 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20181005_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academicprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssc', models.FloatField()),
                ('hsc', models.FloatField()),
                ('cgpa', models.CharField(max_length=5)),
                ('department', models.CharField(max_length=20)),
                ('division', models.CharField(max_length=5)),
                ('rollno', models.CharField(max_length=5)),
                ('desc', models.CharField(max_length=500)),
                ('sum', models.IntegerField()),
            ],
        ),
    ]