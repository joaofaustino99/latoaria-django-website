# Generated by Django 3.2 on 2021-04-28 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_produto_descricao_grande'),
    ]

    operations = [
        migrations.CreateModel(
            name='Morada_envio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('morada', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=200)),
                ('concelho', models.CharField(max_length=200)),
                ('codigo_postal', models.CharField(max_length=200)),
                ('compra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.compra')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.cliente')),
            ],
        ),
    ]
