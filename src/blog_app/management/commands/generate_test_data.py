import random

from django.core.management.base import BaseCommand
from blog_app.models import Article, ArticleTag

from faker import Faker


class Command(BaseCommand):
    help = "Generate test data for benchmarking"

    def add_arguments(self, parser):
        parser.add_argument("--articles", type=int, default=500)
        parser.add_argument("--tags", type=int, default=10)

    def handle(self, *args, **options):
        fake = Faker()

        tags = [
            ArticleTag.objects.create(name=fake.word()) for i in range(options["tags"])
        ]
        for i in range(options["articles"]):
            article = Article.objects.create(
                title=fake.catch_phrase(),
                content="\n\n".join(fake.texts(nb_texts=random.randint(2, 5))),
            )
            article.tags.set(random.sample(tags, k=random.randint(1, 3)))
        self.stdout.write(
            self.style.SUCCESS(
                f"Created {options['articles']} articles and {options['tags']} tags."
            )
        )
