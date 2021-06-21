from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Article
        fields = ['id', 'url', 'title', 'content', 'time', 'author', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.HyperlinkedRelatedField(view_name='article-detail', many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'articles']