# Generated by Django 3.1.1 on 2020-09-27 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0005_auto_20200927_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
