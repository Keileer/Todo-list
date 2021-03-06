# Generated by Django 3.2.6 on 2021-08-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, max_length=1024, null=True)),
                ('deadline', models.DateField()),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
