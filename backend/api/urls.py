from django.urls import include, path
from .views import ArticleList

app_name = 'api'

urlpatterns = [

    path('', ArticleList.as_view(), name='api'),
]
#     path('', include('blog.urls')),
#     path('api/', include('api.urls')),
# ]
