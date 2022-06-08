# Generated by Django 4.0.4 on 2022-06-08 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notaFiscal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('valor', models.IntegerField(max_length=1000000000)),
                ('cpf', models.IntegerField(max_length=11)),
            ],
        ),
    ]
