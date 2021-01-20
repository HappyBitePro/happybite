# Generated by Django 3.1.4 on 2021-01-17 18:32

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('family_memebers_numbers', models.IntegerField(default=1)),
                ('address', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('social_state', models.CharField(choices=[('single', 'single'), ('married', 'married')], max_length=15)),
                ('work_status', models.CharField(choices=[('unemployed', 'unemployed'), ('employed', 'employed')], max_length=15)),
                ('salary', models.IntegerField(default=0)),
            ],
        ),
    ]