# Generated by Django 2.2.2 on 2019-06-05 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eletiva', '0004_auto_20190605_0839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='matricula',
        ),
    ]
