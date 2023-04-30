# Generated by Django 3.2 on 2021-04-20 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_productimage_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='store/static/store/images/'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='imagem',
            field=models.ImageField(upload_to='store/static/store/images/'),
        ),
    ]