# Generated by Django 4.2.16 on 2024-11-18 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeros', models.CharField(max_length=100)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResultadoSorteio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_concurso', models.IntegerField()),
                ('dezenas', models.CharField(max_length=50)),
                ('acertos', models.IntegerField()),
                ('aposta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sorteio.aposta')),
            ],
        ),
    ]
