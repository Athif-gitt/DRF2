from rest_framework import serializers
from .models import Author, Post, Comment

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'user', 'bio']
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']
        extra_kwargs = {
             'id': {'read_only': True}, # extra_kwargs
        }


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many= True, read_only= True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'comments', 'comment_count']

    def get_comment_count(self, obj):
            return obj.comments.count()

        
