# Generated by Django 2.0.5 on 2018-05-27 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('category', models.CharField(choices=[('1', 'Processadores'), ('2', 'Memória RAM'), ('3', 'Disco Rígido/SSD'), ('4', 'Placa de Vídeo'), ('5', 'Gabinete'), ('6', 'Placa mãe'), ('7', 'Fonte')], max_length=1, verbose_name='Categorias')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
            ],
        ),
        migrations.CreateModel(
            name='Stoke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='Quantidade')),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='stoke',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='stoke.Stoke'),
        ),
    ]
