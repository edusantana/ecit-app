# Generated by Django 2.2.2 on 2019-06-05 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0005_auto_20190605_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='matricula',
            field=models.IntegerField(blank=True, default='', verbose_name='Matrícula'),
        ),
    ]