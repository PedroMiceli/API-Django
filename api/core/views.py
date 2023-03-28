from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuarios, Postagens, Comentarios
from .serializers import UsuariosSerializer, PostagensSerializer, ComentariosSerializer

# Create your views here.
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class PostagensViewSet(viewsets.ModelViewSet):
    queryset = Postagens.objects.all()
    serializer_class = PostagensSerializer

class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer