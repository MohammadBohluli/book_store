# Generated by Django 4.2 on 2023-12-23 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('fr', 'Persian'), ('en', 'English')], default='en', max_length=2),
        ),
    ]
