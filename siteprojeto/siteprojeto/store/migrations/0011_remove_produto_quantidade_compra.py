# Generated by Django 3.2 on 2021-04-21 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_produto_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='quantidade_compra',
        ),
    ]
