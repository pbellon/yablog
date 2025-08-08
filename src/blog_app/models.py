# filepath: /home/trb/dev/django-htmx/src/blog/models.py
from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.text import slugify
from markdown import markdown


class ArticleTag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Article(models.Model):
    class Meta:
        indexes = [models.Index(fields=["slug"]), models.Index(fields=["title"])]

    creation_date = models.DateField(auto_now_add=True)
    last_update_date = models.DateField(auto_now=True)
    title = models.CharField(max_length=140)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    tags = models.ManyToManyField(ArticleTag, blank=True)

    content_parsed = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title[0:50])

        self.content_parsed = markdown(
            self.content,
            extensions=["fenced_code", "codehilite"],
            extension_configs={
                "codehilite": {
                    "guess_lang": False,  # don't mis-detect plain code
                    "linenums": False,  # or True if you want line numbers
                    "noclasses": True,  # True -> inline styles (no CSS file needed)
                    "pygments_style": "emacs",  # pick any Pygments style
                }
            },
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class FavoriteArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
