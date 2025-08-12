from django.urls import path, include
from rest_framework import routers

from api.articles import ArticleViewSet, ArticleTagViewSet

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'tags', ArticleTagViewSet, basename='articletag')

def urls():
    return [
        path('api/', include(router.urls)),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]

