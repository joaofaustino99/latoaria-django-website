# Generated by Django 3.2 on 2021-04-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_compra_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemscompra',
            name='quantidade',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
