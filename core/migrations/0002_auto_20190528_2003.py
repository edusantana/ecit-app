# Generated by Django 2.2.1 on 2019-05-28 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='ativo',
            field=models.BooleanField(default=True, max_length=255),
        ),
    ]
