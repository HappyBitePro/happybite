# Generated by Django 3.1.4 on 2021-01-22 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0005_auto_20210122_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='description',
            field=models.TextField(),
        ),
    ]
