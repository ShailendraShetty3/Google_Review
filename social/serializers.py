from rest_framework import serializers
from .models import Posts, Post_Meta, Comment, Users

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class PostsSerializerSerializerPatch(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'
        extra_kwargs = {
            'post_author': {'required': False},
            'post_date': {'required': False},
            'post_name': {'required': False},
            'post_status': {'required': False},
            'post_type': {'required': False},
            'comment_count': {'required': False},
            'like_count': {'required': False},
        }


class Post_MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_Meta
        fields = '__all__'

class Post_MetaSerializerPatch(serializers.ModelSerializer):
    class Meta:
        model = Post_Meta
        fields = '__all__'
        extra_kwargs = {
            'post_id': {'required': False},
            'meta_key': {'required': False},
            'meta_value': {'required': False},
        }

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class UsersSerializerPatch(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {
            'user_login': {'required': False},
            'user_name': {'required': False},
            'display_name': {'required': False},
            'user_email': {'required': False},
            'user_password': {'required': False},
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializerPatch(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'comment_date': {'required': False},
            'post_name': {'required': False},
            'comment_author': {'required': False},
            'comment_author_email': {'required': False},
            'comment_post': {'required': False},
            'user': {'required': False},
        }