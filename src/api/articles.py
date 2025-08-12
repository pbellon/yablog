from rest_framework import routers, serializers, viewsets

from blog_app.models import Article, ArticleTag

class ArticleTagSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='articletag-detail',
        lookup_field='pk',
    )

    class Meta:
        model = ArticleTag
        fields = ['id', 'slug', 'name', 'url']



class ArticleTagViewSet(viewsets.ModelViewSet):
    queryset = ArticleTag.objects.all()
    serializer_class = ArticleTagSerializer


class ArticleListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='article-detail',
        lookup_field='pk',
    )

    class Meta:
        model = Article
        fields = ['id', 'slug', 'title', 'creation_date', 'last_update_date', 'url']


class ArticleDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField(
        style={'base_template': 'textarea.html'}
    )
    content_parsed = serializers.CharField(
        read_only=True,

    )
    creation_date = serializers.DateField(read_only=True)
    last_update_date = serializers.DateField(read_only=True)
    tags = ArticleTagSerializer(many=True, read_only=True)
    tags_slugs = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        queryset=ArticleTag.objects.all(),
        source='tags',
        required=False,
    )

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        article = Article.objects.create(**validated_data)

        if tags_data:
            article.tags.set(tags_data)
    
    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()

        tags_data = validated_data.pop('tags', None)

        if tags_data is not None:
            instance.tags.set(tags_data)

        return instance


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        return ArticleDetailSerializer

    def get_queryset(self):
        queryset = Article.objects.all()

        if self.action == 'list':
            # restricts SQL to only relevant fields
            queryset = queryset.only('id', 'title', 'creation_date', 'last_update_date', 'slug')


        if self.action in ['retrieve', 'update', 'partial_update']:
            queryset = queryset.prefetch_related('tags')

        return queryset
