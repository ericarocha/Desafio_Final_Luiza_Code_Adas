# Generated by Django 3.2.7 on 2021-09-24 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cnpj', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Segmentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Voltagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('tamanho', models.CharField(max_length=15)),
                ('preço', models.CharField(max_length=15)),
                ('quantidade', models.IntegerField()),
                ('imagem', models.ImageField(upload_to='imagens')),
                ('id_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.empresas')),
                ('id_voltagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.voltagens')),
            ],
        ),
        migrations.AddField(
            model_name='empresas',
            name='id_segmento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.segmentos'),
        ),
    ]
