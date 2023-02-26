# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from blog.models import Article
from .permissions import IsSuperUserOrStaffReadOnly, IsAuthorOrReadOnly , IsStaffOrReadOnly
from .serializers import ArticleSerializer, UserSerializer

# Create your views here.


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class RevokeToken(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({"method":"get"})

    def post(self, request):
        return Response({"method":"post"})

    def put(self, request):
        return Response({"method":"put"})
    
    def delete(self, request):
        return Response({"method":"delete"})


    # def delete(self ,request):
    #     request.auth.delete()
    #     return Response(status=204)

    