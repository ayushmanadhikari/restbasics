from django import urls
from rest_framework import urls
from django.urls import path
from django.urls.conf import include
from . import views 


urlpatterns = [
    path('', views.api_root, name='entry'),
    path('aricles/', views.ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail')

]


urlpatterns += [path('api-auth/', include(urls))]

