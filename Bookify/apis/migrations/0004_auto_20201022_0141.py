# Generated by Django 3.1.2 on 2020-10-21 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_books'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='profile',
            new_name='email',
        ),
    ]