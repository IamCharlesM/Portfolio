# Generated by Django 2.0.2 on 2018-04-04 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='Job Title', max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(max_length=255),
        ),
    ]
