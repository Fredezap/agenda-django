# Generated by Django 4.2 on 2023-05-22 20:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('create_date', models.DateField(default=datetime.date.today)),
                ('date_end', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('priority', models.IntegerField(default=0)),
            ],
        ),
    ]
