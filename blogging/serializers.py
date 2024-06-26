from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "author",
            "text",
            "created_date",
            "modified_date",
            "published_date",
        ]
