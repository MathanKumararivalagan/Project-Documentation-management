# Generated by Django 5.0 on 2024-03-14 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reader', '0007_student_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Department',
        ),
    ]
