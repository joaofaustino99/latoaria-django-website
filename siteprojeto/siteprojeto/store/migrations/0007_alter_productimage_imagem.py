# Generated by Django 3.2 on 2021-04-20 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='imagem',
            field=models.ImageField(upload_to='store/static/store/images'),
        ),
    ]