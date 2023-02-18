from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
     #    fields = ('title','slug','author','content','publish','status')
     #    exclude = ('created','updated') #all expect 
        fields = '__all__' #all models fields


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
     #    fields = ('title','slug','author','content','publish','status')
     #    exclude = ('created','updated') #all expect 
        fields = '__all__' #all models fields