from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import HasOwnerRightorReadOnly
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'articles': reverse('article-list', request=request, format=format)
    })

class ArticleListView(ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, HasOwnerRightorReadOnly]


'''
class UserViewSet(ReadOnlyModelViewSet):
    #automatically provides list and retrieve functions
    queryset = User.objects.all()
    serializer_class = UserSerializer
'''


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
