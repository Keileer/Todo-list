# Generated by Django 3.2.6 on 2021-08-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='description',
            field=models.TextField(blank=True, default='My Tasks', max_length=1024, null=True),
        ),
    ]