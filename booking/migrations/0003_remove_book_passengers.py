# Generated by Django 2.1 on 2018-08-22 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_book_passengers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Passengers',
        ),
    ]
