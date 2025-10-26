from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from django.shortcuts import render, get_object_or_404
from .models import Post
from .serializers import PostSerializer

def pagina_inicial(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    
    return render(request, 'core/index.html', context)

def post_detalhes(request, post_pk):
    post = get_object_or_404(Post,pk=post_pk)
    context = {
        'post': post
    } 
    return render(request, 'core/detalhes_post.html', context)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer