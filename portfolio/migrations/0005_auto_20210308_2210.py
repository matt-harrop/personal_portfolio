# Generated by Django 3.1.3 on 2021-03-08 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_experience_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
