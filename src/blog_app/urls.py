from django.urls import path
from django.views.generic import RedirectView, TemplateView
from blog_app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("articles/", RedirectView.as_view(url="/", permanent=True)),
    path("favorite-articles", views.get_favorites_articles, name="favorite_articles"),
    path("paginated-articles", views.paginated_articles, name="paginated_articles"),
    path("articles-by-tag/<slug:slug>", views.articles_by_tag, name="articles_by_tag"),
    path("articles/<slug:slug>", views.article_detail, name="article_detail"),
    path(
        "articles/<slug:slug>/other-articles",
        views.other_articles,
        name="other_articles",
    ),
    path("search", views.search, name="search"),
    path(
        "favorites/add/<int:id>",
        views.add_article_to_favorites,
        name="add_article_to_favorites",
    ),
    path(
        "favorites/remove/<int:id>",
        views.remove_article_from_favorites,
        name="remove_article_from_favorites",
    ),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
