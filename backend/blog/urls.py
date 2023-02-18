from django.urls import path
from .views import ArticleListView, ArticleDetail, UserListView, UserDetail

app_name = 'blog'

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('<int:pk>', ArticleDetail.as_view(), name='detail'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),
]
