# Generated by Django 4.2.8 on 2023-12-04 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='endereco',
            new_name='jogo_favorito',
        ),
        migrations.AddField(
            model_name='cliente',
            name='idade',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
