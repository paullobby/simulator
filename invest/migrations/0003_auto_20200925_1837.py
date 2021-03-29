# Generated by Django 3.1.1 on 2020-09-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0002_featuredstocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
                ('featured', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='FeaturedStocks',
        ),
    ]