from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', default=None)

    def __str__(self):
        return self.title
