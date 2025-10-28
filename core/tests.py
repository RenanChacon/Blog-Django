from django.test import TestCase
from .models import Post

#comentario 
class TestPostModel(TestCase):

    def setUp(self):
      
        self.post = Post.objects.create(
            titulo="Post 1",
            conteudo="Conteúdo do post 1."
        )

    def test_post_criacao(self):
    
        post_do_banco = Post.objects.get(id=self.post.id)
        
        self.assertEqual(post_do_banco.titulo, "Post 1")
        self.assertEqual(post_do_banco.conteudo, "Conteúdo do post 1.")
        
        self.assertEqual(Post.objects.count(), 1)

    def test_str_method(self):

        post_do_banco = Post.objects.get(id=self.post.id)
        
        self.assertEqual(str(post_do_banco), "Post 1")
