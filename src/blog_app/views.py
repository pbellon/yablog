from django.shortcuts import get_object_or_404, render
from markdown import markdown

from blog_app.models import Article, ArticleTag, FavoriteArticle

# root endpoint
def index(request):
    articles = Article.objects.order_by('-creation_date')[:10]
    return render(request, "blog/index.html", { 'articles': articles })

def article_detail(request, slug):
    article = get_object_or_404(Article.objects.prefetch_related('tags'), slug=slug)

    article.has_tags = article.tags.exists()

    # Only try to fetch if count > 0 to minimize number of SQL requests
    if article.has_tags:
        article.all_tags = article.tags.all()

    if request.user.is_authenticated:
        article.favorited = FavoriteArticle.objects.filter(article_id=article.id, user_id=request.user.id).exists()

    return render(request, "blog/article_detail.html", { 'article': article })

def articles(request, n=10):
    articles = Article.objects.order_by('creation_date')[:n]
    return render(request, "blog/articles.html", { 'articles': articles })

def articles_by_tag(request, slug):
    tag = get_object_or_404(ArticleTag, slug=slug)
    articles = Article.objects.filter(tags__id=tag.id)
    return render(request, "blog/articles_by_tag.html", { 'articles': articles, 'tag': tag })

def other_articles(request, slug):
    other_articles_list = []
    current_article = get_object_or_404(Article, slug=slug)
    if current_article.tags.exists():
        all_tags_ids = [tag.id for tag in current_article.tags.all()]
        other_articles_list = Article.objects.exclude(id=current_article.id).filter(tags__id__in=all_tags_ids).distinct()[:10]
    else:    
        other_articles_list = Article.objects.exclude(slug=slug)[:10]

    has_articles = other_articles_list.exists()

    return render(request, 'htmx/other_articles.html', { 'articles': other_articles_list, 'has_articles': has_articles })


def add_article_to_favorites(request, id):
    FavoriteArticle.objects.create(article_id=id, user_id=request.user.id)
    favorites = FavoriteArticle.objects.filter(user_id=request.user.id).select_related('article')
    has_favorites = favorites.exists()
    return render(request, 'htmx/favorites.html', { 'favorites': favorites, 'has_favorites': has_favorites })

def remove_article_from_favorites(request, id):
    FavoriteArticle.objects.filter(article_id=id, user_id=request.user.id).delete()
    favorites = FavoriteArticle.objects.filter(user_id=request.user.id).select_related('article')
    has_favorites = favorites.exists()

    return render(request, 'htmx/favorites.html', { 'favorites': favorites, 'has_favorites': has_favorites })

def get_favorites_articles(request):
    favorites = FavoriteArticle.objects.filter(user=request.user.id).select_related('article')
    has_favorites = favorites.exists()
    
    return render(request, 'htmx/favorites.html', { 'favorites': favorites, 'has_favorites': has_favorites })

def search_nested(request):
    query = request.POST['search']
    results = Article.objects.filter(title__icontains=query)
    has_results = results.exists()
    return render(request, 'htmx/search_results.html', {'results': results, 'has_results': has_results })

