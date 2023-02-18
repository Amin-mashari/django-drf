from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article
from django.contrib.auth.models import User
# Create your views here.


class ArticleListView(ListView):
    def get_queryset(self):
        return Article.objects.filter(status=True)


class ArticleDetail(DetailView):
    def get_object(self):
        return get_object_or_404(Article.objects.filter(status=True), pk=self.kwargs.get('pk'))


class UserListView(ListView):
    def get_queryset(self):
        return User.objects.all()


class UserDetail(DetailView):
    def get_object(self):
        return get_object_or_404(User.objects.all(), pk=self.kwargs.get('pk'))
