# Generated by Django 2.2.5 on 2019-11-06 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_review_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='num_likes',
            field=models.IntegerField(default=0),
        ),
    ]
