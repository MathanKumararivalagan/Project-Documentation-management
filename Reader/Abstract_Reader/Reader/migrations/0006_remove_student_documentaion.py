# Generated by Django 5.0 on 2024-03-14 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reader', '0005_student_documentaion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Documentaion',
        ),
    ]
