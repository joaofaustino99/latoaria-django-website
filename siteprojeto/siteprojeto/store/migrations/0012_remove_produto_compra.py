# Generated by Django 3.2 on 2021-04-21 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_produto_quantidade_compra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='compra',
        ),
    ]