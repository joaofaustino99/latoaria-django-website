# Generated by Django 3.2 on 2021-04-20 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210420_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='tamanho',
        ),
        migrations.AddField(
            model_name='produto',
            name='tamanho',
            field=models.ManyToManyField(to='store.Tamanho'),
        ),
    ]
