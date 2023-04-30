# Generated by Django 3.2 on 2021-04-15 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210415_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='compra_fk',
        ),
        migrations.RemoveField(
            model_name='quantidade_total',
            name='id',
        ),
        migrations.AddField(
            model_name='produto',
            name='compra',
            field=models.ManyToManyField(to='store.Compra'),
        ),
        migrations.AlterField(
            model_name='quantidade_total',
            name='produto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='store.produto'),
        ),
    ]
