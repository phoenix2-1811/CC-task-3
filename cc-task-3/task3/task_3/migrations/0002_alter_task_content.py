# Generated by Django 5.0.6 on 2024-07-10 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.CharField(max_length=100),
        ),
    ]