# Generated by Django 2.0.2 on 2018-04-06 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180406_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='url',
            field=models.TextField(default='link pls'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(),
        ),
    ]