# Generated by Django 3.0.7 on 2020-07-13 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200713_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]