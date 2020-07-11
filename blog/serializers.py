from rest_framework import serializers
from .models import Post


class PostSeriazizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["author", "title", "text", "theme"]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get("author", instance.author)
        instance.title = validated_data.get("title", instance.title)
        instance.text = validated_data.get("text", instance.text)
        instance.theme = validated_data.get("theme", instance.theme)

        instance.save()
        return instance
