from django.db import models
from uuid import uuid4

# Create your models here.
class Usuarios(models.Model):
    id_Usuario = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=20)
    rua = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)
    cep = models.IntegerField()
    email = models.EmailField(max_length=255)
    prestador = models.BooleanField(default=False)
    objects=models.Manager()

    def __str__(self):
        return self.nome

class Postagens(models.Model):
    id_Postagem = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    mensagem = models.CharField(max_length=255)
    id_Usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.mensagem

class Comentarios(models.Model):
    id_Comentario = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    comentario = models.CharField(max_length=250)
    id_Usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_Postagem = models.ForeignKey(Postagens, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.comentario