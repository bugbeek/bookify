# Generated by Django 3.1.2 on 2020-10-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0008_auto_20201024_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
