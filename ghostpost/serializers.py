from rest_framework import serializers
from .models import Post

overall_votes = serializers.ReadOnlyField()


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "post_type",
            "body",
            "upvotes",
            "downvotes",
            "overall_votes",
            "post_date",
        ]
