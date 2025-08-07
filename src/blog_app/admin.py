from django.contrib import admin

from blog_app import models

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'id' )
    list_filter = ['title', 'tags']
    exclude = ('content_parsed',)
    ordering = ['-last_update_date',]


@admin.register(models.ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'id')
    list_filter = ['name']
    ordering = ['name']