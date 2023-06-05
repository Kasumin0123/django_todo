# Generated by Django 4.2.1 on 2023-06-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todo_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='scheduledTime',
        ),
        migrations.AddField(
            model_name='todo',
            name='dueDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='dueTime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
