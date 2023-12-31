# Generated by Django 4.2.4 on 2023-08-31 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=10)),
                ('nome_empresa', models.CharField(max_length=200)),
                ('categoria_empresa', models.CharField(max_length=200)),
                ('quitado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(max_length=500)),
                ('valor', models.FloatField()),
            ],
        ),
    ]
