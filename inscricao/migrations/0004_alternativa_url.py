# Generated by Django 2.2.2 on 2019-06-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0003_remove_alternativa_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='alternativa',
            name='url',
            field=models.URLField(blank=True, verbose_name='Link para mais informações'),
        ),
    ]