# Generated by Django 3.1.1 on 2020-09-25 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0003_auto_20200925_1837'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stocks',
            new_name='Stock',
        ),
    ]
