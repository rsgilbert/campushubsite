# Generated by Django 2.2.5 on 2019-10-15 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchhistory',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]