# Generated by Django 3.2 on 2021-04-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_compra_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
