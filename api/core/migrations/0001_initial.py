# Generated by Django 4.1.7 on 2023-03-24 13:54

from django.db import migrations, models
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_Usuario', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=20)),
                ('rua', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('uf', models.CharField(max_length=255)),
                ('cep', models.IntegerField(max_length=8)),
                ('email', models.EmailField(max_length=255)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
