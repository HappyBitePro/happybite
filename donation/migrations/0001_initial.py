# Generated by Django 3.1.4 on 2021-01-03 19:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Slug', models.SlugField(blank=True, null=True)),
                ('Food_Type', models.CharField(max_length=20)),
                ('Packing_Type', models.CharField(choices=[('Packed', 'Packed'), ('Not Packed', 'Not Packed')], max_length=15)),
                ('Deliver_Type', models.CharField(choices=[(' Delivery', ' Delivery'), ('No Delivery', 'No Delivery')], max_length=15)),
                ('Donate_Date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Expiry_Date', models.DateTimeField()),
                ('Available', models.BooleanField(default=True)),
                ('charity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.charityprofile')),
                ('donor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.donorprofile')),
            ],
        ),
    ]
