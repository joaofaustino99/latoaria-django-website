# Generated by Django 3.2 on 2021-04-21 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_alter_compra_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='data',
        ),
    ]