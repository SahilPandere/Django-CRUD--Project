# Generated by Django 4.1.4 on 2023-01-19 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=15)),
                ('sid', models.IntegerField()),
                ('saddress', models.CharField(max_length=15)),
            ],
        ),
    ]