# Generated by Django 3.1.4 on 2021-01-23 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0004_auto_20210123_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiary',
            name='user',
        ),
    ]
