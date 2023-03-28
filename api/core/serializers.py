from rest_framework import serializers
from .models import Usuarios, Postagens

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class PostagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagens
        fields = '__all__'