# Generated by Django 4.2.6 on 2024-08-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('datetime', models.DateTimeField()),
                ('people', models.IntegerField(choices=[(1, 'People 1'), (2, 'People 2'), (3, 'People 3')])),
                ('special_request', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
