# Generated by Django 3.0.8 on 2020-07-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book1', '0015_auto_20200717_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book2',
            name='Book_genre',
            field=models.CharField(choices=[('Thriller', 'Thriller'), ('Romance', 'Romance'), ('Fiction', 'Fiction')], default='Thriller', max_length=20),
        ),
    ]
