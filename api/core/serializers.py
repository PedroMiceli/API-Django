from rest_framework import serializers
from .models import Usuarios, Postagens, Comentarios

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class PostagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagens
        fields = '__all__'


class ComentariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comentarios
        fields = '__all__'
