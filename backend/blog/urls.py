from django.urls import path
from .views import ArticleListView,ArticleDetail

app_name = 'blog'

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('<int:pk>', ArticleDetail.as_view(), name='detail'),
]