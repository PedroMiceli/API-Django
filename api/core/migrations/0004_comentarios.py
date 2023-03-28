# Generated by Django 4.1.7 on 2023-03-28 18:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_usuarios_prestador_postagens'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id_Comentario', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comentario', models.CharField(max_length=250)),
                ('id_Postagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.postagens')),
                ('id_Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuarios')),
            ],
        ),
    ]
