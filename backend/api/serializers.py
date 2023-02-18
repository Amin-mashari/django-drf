from rest_framework import serializers
from blog.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
     #    fields = ('title','slug','author','content','publish','status')
     #    exclude = ('created','updated') #all expect 
        fields = '__all__' #all models fields