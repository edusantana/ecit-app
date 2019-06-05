# Generated by Django 2.2.1 on 2019-06-04 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_auto_20190604_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='EletivaConfiguracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio_selecao', models.DateTimeField(verbose_name='Data da selecao')),
                ('quantidade_maxima', models.PositiveSmallIntegerField(verbose_name='Quantidade máxima de inscrições por eletiva')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Periodo')),
            ],
        ),
        migrations.CreateModel(
            name='Eletiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('professor', models.CharField(max_length=255)),
                ('configuracao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eletivas', to='eletiva.EletivaConfiguracao')),
            ],
        ),
    ]