# Generated by Django 3.1.7 on 2021-03-30 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=64)),
                ('day', models.CharField(max_length=32)),
                ('prediction', models.IntegerField()),
            ],
        ),
    ]
