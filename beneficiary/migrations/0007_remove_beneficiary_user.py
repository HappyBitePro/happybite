# Generated by Django 3.1.4 on 2021-01-23 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0006_beneficiary_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiary',
            name='user',
        ),
    ]
