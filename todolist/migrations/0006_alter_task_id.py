# Generated by Django 4.1 on 2022-09-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_alter_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
