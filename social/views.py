from django.http import JsonResponse
from .models import Posts, Post_Meta, Comment, Users
from rest_framework import status,generics,parsers
from django.shortcuts import get_object_or_404
from .serializers import PostsSerializer, Post_MetaSerializer, CommentSerializer, UsersSerializer, UsersSerializerPatch


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



from drf_yasg.utils import swagger_auto_schema
       

class PostListCreateView(generics.GenericAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    parser_classes = [parsers.MultiPartParser]

    def get(self, request, format=None):
        user = Posts.objects.all()
        serializer = PostsSerializer(user, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PostDetail(generics.GenericAPIView):
    serializer_class = PostsSerializer   #this serializer object
    parser_classes = [parsers.MultiPartParser]
    def get_object(self, id):
        try:
            return Posts.objects.get(pk=id)
        except Posts.DoesNotExist:
            return None
    
    def get(self, request, id, format=None):
        post = self.get_object(id)
        if post:
            serializer = self.get_serializer(post).data   #this point out to previous mentioned
            return Response(serializer)
        return Response(status=status.HTTP_404_NOT_FOUND)



    def put(self, request, id, format=None):
        post = get_object_or_404(Posts, pk=id)
        serializer = PostsSerializer(post, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id, format=None):
        user = self.get_object(id)
        if user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

#post meta 

class Post_MetaListCreateView(generics.GenericAPIView):
    queryset = Post_Meta.objects.all()
    serializer_class = Post_MetaSerializer
    parser_classes = [parsers.MultiPartParser]

    def get(self, request, format=None):
        user = Post_Meta.objects.all()
        serializer = Post_MetaSerializer(user, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class Post_MetaDetail(generics.GenericAPIView):
    parser_classes = [parsers.MultiPartParser]

    def get_object(self, id):
        try:
            return Post_Meta.objects.get(pk=id)
        except Post_Meta.DoesNotExist:
            return None
    
    def get(self, request, id, format=None):
        post = self.get_object(id)
        if post:
            serializer = Post_MetaSerializer(post)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)



    def put(self, request, id, format=None):
        post = get_object_or_404(Post_Meta, pk=id)
        serializer = Post_MetaSerializer(post, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id, format=None):
        user = self.get_object(id)
        if user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

#comment
    
class CommentListCreateView(generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    parser_classes = [parsers.MultiPartParser]

    def get(self, request, format=None):
        user = Comment.objects.all()
        serializer = CommentSerializer(user, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CommentDetail(generics.GenericAPIView):
    parser_classes = [parsers.MultiPartParser]

    def get_object(self, id):
        try:
            return Comment.objects.get(pk=id)
        except Comment.DoesNotExist:
            return None
    
    def get(self, request, id, format=None):
        post = self.get_object(id)
        if post:
            serializer = CommentSerializer(post)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)



    def put(self, request, id, format=None):
        post = get_object_or_404(Comment, pk=id)
        serializer = CommentSerializer(post, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id, format=None):
        user = self.get_object(id)
        if user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
#users
    
class UserListCreateView(generics.GenericAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    parser_classes = [parsers.MultiPartParser]

    def get(self, request, format=None):
        user = Users.objects.all()
        serializer = UsersSerializer(user, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class UsertDetail(generics.GenericAPIView):
    parser_classes = [parsers.MultiPartParser]

    def get_object(self, id):
        try:
            return Users.objects.get(pk=id)
        except Users.DoesNotExist:
            return None
    
    def get(self, request, id, format=None):
        post = self.get_object(id)
        if post:
            serializer = UsersSerializer(post)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)


    @swagger_auto_schema(
        request_body=UsersSerializerPatch,
        responses={
            200: "Success",
            400: "Bad Request",
            404: "Not Found"
        }
    )
    def patch(self, request, id, format=None):
        user = self.get_object(id)
        if user:
            serializer = UsersSerializerPatch(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(
        request_body=UsersSerializer,
        responses={
            200: "Success",
            400: "Bad Request",
            404: "Not Found"
        }
    )
    def put(self, request, id, format=None):
        post = get_object_or_404(Users, pk=id)
        serializer = UsersSerializer(post, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id, format=None):
        user = self.get_object(id)
        if user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    

