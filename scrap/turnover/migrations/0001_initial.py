# Generated by Django 5.0.1 on 2024-01-26 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=200)),
                ('turnover', models.CharField(max_length=200)),
                ('ltp', models.CharField(max_length=200)),
                ('change', models.CharField(max_length=200)),
                ('high', models.CharField(max_length=200)),
                ('low', models.CharField(max_length=200)),
                ('open', models.CharField(max_length=200)),
                ('qty', models.CharField(max_length=200)),
            ],
        ),
    ]