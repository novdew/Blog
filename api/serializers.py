from rest_framework import serializers
from pages.models import Post


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=40)
    body = serializers.CharField(max_length=1000)
    image = serializers.ImageField()

    class Meta:
        model = Post
        fields = ['title', 'body', 'image']