from rest_framework import serializers
from .models import Post

class PostSeriazizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

"""class PostSeriazizer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    text = serializers.CharField()
    theme = serializers.CharField()
    author_id = serializers.IntegerField()"""
    