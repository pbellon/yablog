from django.urls import path

from blog_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles', views.articles, name='articles'),
    path('favorite-articles', views.get_favorites_articles, name='favorite_articles'),
    path('articles-by-tag/<slug:slug>', views.articles_by_tag, name='articles_by_tag'),
    path('articles/<slug:slug>', views.article_detail, name='article_detail'),
    path('articles/<slug:slug>/other-articles', views.other_articles, name='other_articles'),
    path('search-nested', views.search_nested, name='search_nested'),
    path('add-to-favorites/<int:id>', views.add_article_to_favorites, name='add_article_to_favorites'),
    path('remove-from-favorites/<int:id>', views.remove_article_from_favorites, name='remove_article_from_favorites')
]