# Generated by Django 4.1.2 on 2022-10-22 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='progress',
            field=models.IntegerField(null=True),
        ),
    ]
