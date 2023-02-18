# from django.shortcuts import render
from rest_framework.generics import ListAPIView
from blog.models import Article
from .serializers import ArticleSerializer

# Create your views here.
class ArticleList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    