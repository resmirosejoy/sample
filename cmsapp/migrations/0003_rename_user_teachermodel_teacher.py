# Generated by Django 4.2.1 on 2023-06-14 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0002_teachermodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachermodel',
            old_name='User',
            new_name='teacher',
        ),
    ]
