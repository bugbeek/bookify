# Generated by Django 3.1.2 on 2020-10-21 16:06

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Contact',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
