# Generated by Django 5.0.2 on 2024-02-07 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_rename_datetime_task_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(choices=[(True, 'Done'), (False, 'Not done')], default=False),
        ),
    ]
