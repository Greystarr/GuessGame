# Generated by Django 4.0.4 on 2022-04-23 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess', models.CharField(max_length=5)),
                ('key', models.CharField(max_length=5)),
                ('cncp', models.IntegerField(default=0)),
                ('cnwp', models.IntegerField(default=0)),
                ('essay', models.IntegerField(default=0)),
            ],
        ),
    ]
