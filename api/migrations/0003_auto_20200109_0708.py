# Generated by Django 3.0.2 on 2020-01-09 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_task_taskgroup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tasks',
            new_name='taskgroupid',
        ),
    ]
