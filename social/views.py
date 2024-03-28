from django.http import JsonResponse
from .models import Posts
from rest_framework import status,generics,parsers
from django.shortcuts import get_object_or_404
from .serializers import PostsSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
       

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
    
