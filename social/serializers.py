from rest_framework import serializers
from .models import Posts, Post_Meta, Comment, Users

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class Post_MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_Meta
        fields = '__all__'

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