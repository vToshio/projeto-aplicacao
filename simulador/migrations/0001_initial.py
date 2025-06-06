# Generated by Django 5.2 on 2025-05-27 20:59

import datetime
import django.core.validators
import django.db.models.deletion
import simulador.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Cidade')),
            ],
            options={
                'db_table': 'cidades',
            },
        ),
        migrations.CreateModel(
            name='Concessionaria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='Nome da Concessionária')),
                ('te', models.FloatField(validators=[simulador.validators.validar_positivo], verbose_name='Tarifa TE (R$)')),
                ('tusd', models.FloatField(validators=[simulador.validators.validar_positivo], verbose_name='Tarifa TUSD (R$)')),
                ('atualizada_em', models.DateField(default=datetime.date.today, verbose_name='Atualizada em')),
            ],
            options={
                'db_table': 'concessionarias',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sigla', models.CharField(max_length=2, unique=True, verbose_name='Sigla do Estado')),
            ],
            options={
                'db_table': 'estados',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=30, unique=True, verbose_name='Nome')),
            ],
            options={
                'db_table': 'marcas',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cep', models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(message='Insira apenas os 8 dígitos do CEP', regex='[\\d]{8}')], verbose_name='CEP')),
                ('logradouro', models.CharField(blank=True, max_length=100, null=True, verbose_name='Logradouro')),
                ('hsp', models.FloatField(null=True, verbose_name='Horas de Sol Pleno (kW/m²/mês)')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulador.cidade')),
            ],
            options={
                'db_table': 'enderecos',
            },
        ),
        migrations.AddField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulador.estado'),
        ),
        migrations.CreateModel(
            name='PainelSolar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Nome do Painel')),
                ('valor', models.FloatField(validators=[simulador.validators.validar_positivo], verbose_name='Valor (R$)')),
                ('potencia', models.FloatField(validators=[simulador.validators.validar_positivo], verbose_name='Potência (W)')),
                ('eficiencia', models.FloatField(blank=True, null=True, validators=[simulador.validators.validar_positivo], verbose_name='Eficiência (%)')),
                ('data_consulta', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Data de Consulta')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link de Referência')),
                ('marca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='simulador.marca')),
            ],
            options={
                'db_table': 'paineis_solares',
            },
        ),
        migrations.CreateModel(
            name='Simulacao',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('conta_luz', models.FloatField(validators=[simulador.validators.validar_positivo], verbose_name='Valor da Conta de Luz (R$)')),
                ('area_disponivel', models.FloatField(blank=True, default=40.0, null=True, validators=[simulador.validators.validar_positivo], verbose_name='Área para Instalação (m²)')),
                ('concessionaria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='simulador.concessionaria')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='simulador.endereco')),
                ('painel_solar', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='simulador.painelsolar')),
            ],
            options={
                'db_table': 'simulacoes',
            },
        ),
    ]
