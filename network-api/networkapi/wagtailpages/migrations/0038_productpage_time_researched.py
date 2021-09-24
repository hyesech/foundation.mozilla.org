# Generated by Django 3.1.11 on 2021-09-24 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0037_productpage_mozilla_says'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpage',
            name='time_researched',
            field=models.PositiveIntegerField(default=0, help_text='How many hours were spent researching this product?'),
        ),
    ]
