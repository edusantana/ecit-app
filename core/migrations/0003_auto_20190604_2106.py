# Generated by Django 2.2.1 on 2019-06-04 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190528_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]