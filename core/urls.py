from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('', views.pagina_inicial, name = 'inicio'),
    path('post/<int:post_pk>/', views.post_detalhes, name= 'post_detalhes'),
    path('api/', include(router.urls))
]
