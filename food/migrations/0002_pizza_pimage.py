# Generated by Django 5.0.7 on 2024-07-23 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='pImage',
            field=models.URLField(default='https://example.com/default.jpg'),
        ),
    ]
