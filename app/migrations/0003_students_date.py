# Generated by Django 4.2.7 on 2023-12-19 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_books_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='date',
            field=models.DateField(default='2023-12-19'),
        ),
    ]
